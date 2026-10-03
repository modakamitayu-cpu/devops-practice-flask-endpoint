# Day 7 — Terraform Architecture Review

## Situation
A proposed application workload was placed in a subnet called public,
but the design did not guarantee direct internet connectivity.

## Task
Review routing, addressing and security controls and identify the
missing requirement.

## Action
- Verified the subnet's route-table association.
- Confirmed the default route pointed to the internet gateway.
- Reviewed map_public_ip_on_launch.
- Confirmed that security groups permit traffic but do not provide
  IP addresses or routing.
- Compared a directly public instance with a load-balancer design.

## Result
Terraform formatting: terraform fmt
Terraform validation: terraform validate
Plan: terraform plan
Finding: a public route alone does not provide direct IPv4 internet
access without a public IPv4 address.

## Production improvements
- Use multiple Availability Zones.
- Keep application workloads private.
- Place a load balancer in public subnets.
- Keep PostgreSQL in private database subnets.
- Use secured remote Terraform state.