# OpenShift auto-heal

OpenShift automatic healing example.

# Role variables

For default values, see [`defaults/main.yaml`](defaults/main.yml).

- `openshift_autoheal_state`: present - install/update. absent - uninstall.

- `openshift_autoheal_namespace`: Namespace where the components will be
  deployed.

- `openshift_autoheal_alert_pattern`: Regular expression that alerts names (the
  value of the `alertname` label) should match for them to be proessed by the
  auto-heal mechanism.

- `openshift_autoheal_awx_host`: The host name or IP address of the AWX server
  that will run the auto-heal playbooks.

- `openshift_autoheal_awx_port`: The port number of the AWX server.

- `openshift_autoheal_awx_admin`: The name of the AWX administrator that has
  permissions to create the orgainization, team, user and project that will be
  used by the auto-heal service.

- `openshift_autoheal_awx_admin_password`: The password of the AWX
  administrator.

- `openshift_autoheal_awx_user`: The name of the AWX user that will be used to
  run the auto-heal playbooks.

- `openshift_autoheal_awx_user_password`: The password of the AWX user.

- `openshift_autoheal_awx_project`: The name of the AWX project that contains
  the auto-heal playbook.

- `openshift_autoheal_awx_inventory`: The name of the AWX inventory that contains
  the hosts corresponding to the nodes of the cluster.

- `openshift_autoheal_awx_scm_url`: The URL of the repository that contains the
  auto-heal playbooks.

- `openshift_autoheal_awx_template`: The name of the AWX job template that will
  be created to run the auto-heal playbook.

## Example playbook

```yaml
- name: Deploy the auto-heal example
  hosts: oo_first_master
  remote_user: root
  vars:
    openshift_autoheal_alert_pattern: "MyAlert"
    openshift_autoheal_awx_host: "myawx.example.com"
    openshift_autoheal_awx_admin: "admin"
    openshift_autoheal_awx_admin_password: "..."
    openshift_autoheal_awx_scm_url: "git://gitub.com/myname/myproject"
  roles:
  - openshift_autoheal
```

## License

Apache license, version 2.0.
