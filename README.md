## This is simple 3 end point app

## Create Envioronment
cd devops-practice
python3 -m venv .venv
source .venv/bin/activate
python -m pip install Flask
python -m pip freeze > requirements.txt

## How to statr application
python -m flask --app app run --host 127.0.0.1 run --port 5000

-->
APP_READY=false python -m flask --app app run --port 5000

-->
APP_READY=true python -m flask --app app run --port 5000

*** Verify that "/ready" returns 200 again. This flag only simulates readiness; it does not block requests to "/"

## Expected Endpoint Responce is
>> curl -i http://127.0.0.1:5000
responses --> HTTP/1.1 200 OK
Server: Werkzeug/3.1.8 Python/3.14.4
Date: Sun, 27 Sep 2026 05:48:21 GMT
Content-Type: application/json
Content-Length: 48
Connection: close

>> curl -i http://127.0.0.1:5000/health
responses --> HTTP/1.1 200 OK
Server: Werkzeug/3.1.8 Python/3.14.4
Date: Sun, 27 Sep 2026 05:45:16 GMT
Content-Type: application/json
Content-Length: 19
Connection: close

>> curl -i http://127.0.0.1:5000/ready
responses --> HTTP/1.1 200 OK
Server: Werkzeug/3.1.8 Python/3.14.4
Date: Sun, 27 Sep 2026 05:46:11 GMT
Content-Type: application/json
Content-Length: 19
Connection: close

>> curl -i http://127.0.0.1:5000/ready
responses --> HTTP/1.1 503 SERVICE UNAVAILABLE
Server: Werkzeug/3.1.8 Python/3.14.4
Date: Sun, 27 Sep 2026 05:45:26 GMT
Content-Type: application/json
Content-Length: 22
Connection: close