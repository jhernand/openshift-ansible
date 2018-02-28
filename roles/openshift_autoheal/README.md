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
  that will run the auto-heal playbook.

- `openshift_autoheal_awx_port`: The port number of the AWX server.

- `openshift_autoheal_awx_user`: The name of the AWX user.

- `openshift_autoheal_awx_password`: The password of the AWX user.

- `openshift_autoheal_awx_project`: The name of the AWX project that contains
  the auto-heal playbook.

- `openshift_autoheal_awx_template`: The name of the AWX job template that will
  be created to run the auto-heal playbook.

## Example playbook

```yaml
- name: Deploy the auto-heal example
  hosts: oo_first_master
- hosts: master
  remote_user: root
  vars:
    openshift_autoheal_alert_pattern: "MyAlert"
    openshift_autoheal_awx_host: "myawx.example.com"
    openshift_autoheal_awx_port: "443"
    openshift_autoheal_awx_user: "myuser"
    openshift_autoheal_awx_password: "..."
    openshift_autoheal_awx_project: "My project"
    openshift_autoheal_awx_template: "My template"
  roles:
  - openshift_autoheal
```

## License

Apache license, version 2.0.
