Situation:
A simulated release changed the startup module to gunicorn_typo.

Task:
Find why the new container repeatedly exited and restore a healthy rollout.

Action:
Failing pod:
Current/previous log evidence:
Termination reason:
Exit code:
Restart count:
Event message:
Recovery command:

Result:
Final ready replicas:
GET /:
GET /health:
GET /ready:
Service endpoint readiness:
Did old replicas remain available?:
Time taken to diagnose and recover:

Learning:
CrashLoopBackOff is a symptom. Logs and termination details identify
the cause. Recreating a pod without correcting its configuration
does not resolve the underlying problem.