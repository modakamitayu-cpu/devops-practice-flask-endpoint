# Day 6 — Terraform Variables and Security Groups

## Situation
During a Terraform security review, I found PostgreSQL port 5432
permitted from 0.0.0.0/0.

## Task
Restrict database access so only the application workload could
initiate PostgreSQL connections.

## Action
I reviewed the ingress source, port and destination security group.
Terraform validation passed because the configuration was valid but
insecure. I replaced the public CIDR rule with a reference to the
application security group and validated the configuration again.

## Result
Formatting result: terraform fmt
Validation result: terraform validate
AWS plan: terraform plan
Final database source: application security group only

## Learning
Terraform validation checks syntax and consistency, not business
intent or least-privilege security.