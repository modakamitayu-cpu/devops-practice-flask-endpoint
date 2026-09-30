# Day 4 — Compose, PostgreSQL and Persistence

## Situation
I simulated a database outage in my local Flask/PostgreSQL stack.

## Task
Identify the failed component and restore database readiness.

## Action
- Compared /health and /ready responses.
- Checked service status and application/database logs.
- Identified the stopped database service.
- Started PostgreSQL and repeated the readiness check.


## Learning
The app can remain alive while a dependency is unavailable.
Compose services connect using service names.
Named volumes preserve data beyond a container's lifecycle.