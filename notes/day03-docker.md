# Day 3 — Docker Container and Port Troubleshooting
Date: 29 September 2026

## Objective
Package my Flask application into a Docker image, run it as a
non-root user, and troubleshoot an incorrect port mapping.

## Build
Command:
docker build --pull -t devops-practice:day3 .

I initially used the invalid useradd option --no-cache-home.
I corrected it to --no-create-home and rebuilt the image.

Build result: [successful / error observed]

## Non-root User Verification
Command:
docker run --rm devops-practice:day3 id

Actual output: [paste output here]
Expected UID and GID: 10001

## Container Port Mapping
The application listens on port 8000 inside each container.

- Working container: host 8080 → container 8000.
- Broken lab container: host 8081 → container 9000.
- Corrected mapping: host 8081 → container 8000.

“Broken” was the container name chosen for the failure exercise.
Its application was running, but the port mapping was incorrect.

## STAR — Troubleshooting Exercise

### Situation
I deliberately started a container with an incorrect port mapping.
The container was running, but its health endpoint was unreachable
through host port 8081.

### Task
Identify whether the failure came from the application or the
Docker port configuration, then restore access.

### Action
1. Checked application startup logs with docker logs.
2. Checked the published ports with docker port.
3. Tested /health inside the container on port 8000.
4. Compared the application port with the mapped destination port.
5. Recreated the lab container with mapping 8081:8000.
6. Tested /health again from the host.

### Result
Internal health-check status: [enter observed status]
Host health-check status after correction: [enter observed status]
Actual recovery time: [enter time, or omit if not measured]

## Key Learning
- A running container does not guarantee the app is reachable.
- Host and container ports can differ.
- The mapped container port must match the application listener.
- EXPOSE documents a port; it does not publish it.
- Non-root execution reduces application privileges.
- Two containers are different from two Gunicorn worker processes.

## Prevention
Review port mappings and run an HTTP smoke check after deployment.