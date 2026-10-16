Situation:
A deliberate Service selector change interrupted access to Flask.

Task:
Identify the failing layer and restore access.

Action:
Compared Service selectors with pod labels.
Checked EndpointSlices.
Tested DNS separately from HTTP.
Checked Flask directly on localhost.
Restored the correct Service manifest.

Result:
DNS result:
HTTP result during the fault:
Endpoint addresses during the fault:
Endpoint addresses after recovery:
Final /, /health and /ready status codes:
Time taken to diagnose and recover:

Root cause:
What I would check first next time: