# Day 8 — Local Kubernetes Cluster

## Situation
kubectl could not find the expected kind-devops-lab context, although
the local kind cluster still existed.

## Task
Determine whether the Kubernetes cluster was unavailable or whether
the failure was limited to the local kubeconfig.

## Action
- Listed the available kubectl contexts.
- Confirmed the devops-lab cluster existed with kind.
- Confirmed the control-plane container was running in Docker.
- Restored the expected context name.
- Selected the correct context and default namespace.
- Verified the Kubernetes node and system pods.

## Result
Cluster name: Command: kind get clusters, response: cluster name.

Current context: Command: kubectl config current-context, Respose: Context Name.

Node status: Command: kubectl get nodes, Response: Status Showing Ready.

System pods: Command: kubectl get pods -n kube-system, Response: List Of Name services.

Default namespace: kubectl config view --minify -o 'jsonpath={..namespace}{"\n"}', Response: Showing Name space name.

Final kubectl command: Command: kubectl get nodes, Respose: Showing Contrl Plane Status.

## Learning
A kubeconfig or context problem can prevent kubectl access even when
the cluster and its control-plane container are healthy.