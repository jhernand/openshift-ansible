# OpenShift Prometheus Operator

OpenShift Prometheus Operator manages the operator deployment.

# Requirements

Ansible 2.2

# Role Variables

| Name                                    | Default                |                  |
|----------------|------------------------|------------------|
|                |                        |                  |

# Dependencies

- lib_openshift
- openshift_facts

# Example Playbook

```
---
- name: Deploy Prometheus Operator
  hosts: oo_first_master
  roles:
  - role: openshift_prometheus_operator
```

# License

Apache License, Version 2.0
