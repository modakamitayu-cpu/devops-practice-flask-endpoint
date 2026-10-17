import psycopg
import pytest

import app as app_module


@pytest.fixture()
def client():
    app_module.app.config.update(TESTING=True)

    with app_module.app.test_client() as test_client:
        yield test_client


def test_index_returns_service_information(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {
        "service": "devops-practice",
        "version": "1.0.0",
    }


def test_health_returns_alive(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "alive"}


def test_ready_without_database_configuration(client, monkeypatch):
    monkeypatch.setenv("APP_READY", "true")
    monkeypatch.delenv("DB_HOST", raising=False)

    response = client.get("/ready")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ready",
        "database": "not_configured",
    }


def test_ready_when_application_is_disabled(client, monkeypatch):
    monkeypatch.setenv("APP_READY", "false")
    monkeypatch.delenv("DB_HOST", raising=False)

    response = client.get("/ready")

    assert response.status_code == 503
    assert response.get_json() == {
        "status": "not_ready",
        "reason": "disabled",
    }


def test_ready_when_database_is_unavailable(client, monkeypatch):
    monkeypatch.setenv("APP_READY", "true")
    monkeypatch.setenv("DB_HOST", "postgres")
    monkeypatch.setenv("DB_PORT", "5432")
    monkeypatch.setenv("DB_NAME", "devops")
    monkeypatch.setenv("DB_USER", "devops")
    monkeypatch.setenv("DB_PASSWORD", "dummy-test-password")

    def failed_connection(*args, **kwargs):
        raise psycopg.OperationalError("simulated database failure")

    monkeypatch.setattr(app_module.psycopg, "connect", failed_connection)

    response = client.get("/ready")

    assert response.status_code == 503
    assert response.get_json() == {
        "status": "not_ready",
        "database": "unavailable",
    }