# Day 5 — AWS Network Configuration with Terraform

## Situation
I reviewed a lab network where the public subnet was incorrectly
associated with the private route table.

## Task
Find the routing error and correct the intended network design.

## Action
- Checked the subnet-to-route-table association.
- Located the internet gateway route.
- Confirmed validation could pass despite incorrect routing intent.
- Restored the public subnet's association to the public route table.

## Result
Formatting check: terraform frm --check
Validation: terraform validate
AWS plan: terraform plan
Deployment: terraform apply

## Learning
Resource names do not determine subnet connectivity.
Valid Terraform does not guarantee a correct architecture.