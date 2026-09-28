## Startup command:
I started the Flask app in the background using:
APP_READY=true PYTHONUNBUFFERED=1 nohup .venv/bin/python \
  -m flask --app app run --host 127.0.0.1 --port 8000 \
  --no-reload > logs/app.log 2>&1 &

## Process PID and listening address:
PID: 37704
Listening address: 127.0.0.1:8000
The application accepts connections through the local loopback interface.

## CPU and memory observations:
CPU: 0.1 %CPU
Memory: 1.8 %MEM
Resident memory: 36188 RSS KiB


## Log evidence:
The logs recorded requests to /health and /ready with HTTP 200.
A request to /missing returned HTTP 404 because that route is not defined.


## Port-conflict error:
Starting a second Flask instance on the same address and port failed.
Exact error: Address already in use
Port 8000 is in use by another program. Either identify and stop that program, or start the server with a different port.

## Root cause:
The first Flask process already owned 127.0.0.1:8000.
The second instance could not bind to the same address and port.
The original instance continued responding to health checks.

## Recovery steps:
1. Used ss to identify the process listening on port 8000.
2. Checked its PID and command using ps.
3. Sent SIGTERM to the identified lab process.
4. Verified that the listener disappeared.
5. Restarted Flask and captured its new PID.
6. Checked /health and reviewed the logs.

## Final health-check result:
Command: curl --max-time 5 -i http://127.0.0.1:8000/health
