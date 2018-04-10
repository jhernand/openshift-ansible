# OpenShift Auto-heal Service

The OpenShift Auto-heal Service recevies alert notifications from the
[Prometheus alert manager](https://prometheus.io/docs/alerting/alertmanager) and
tries to solve the root cause executing Ansible
[Tower](https://www.ansible.com/products/tower) or
[AWX](https://github.com/ansible/awx) jobs.

# Installation

See the [installation playbook](../../playbooks/openshift-autoheal) uses the
following variables:

- `openshift_autoheal_deploy`: `true` - install/update. `false` - uninstall.
  Defaults to `false`.

- `openshift_autoheal_namespace`: Namespace where the components will be
  deployed. Defaults to `openshift-autoheal`.

- `openshift_autoheal_name`: Prefix for the names for the objects that compose
  the the auto-heal service. Defaults to `autoheal`.

- `openshift_autoheal_awx_address`: The URL of the Ansible Tower or AWX server
  that will run the auto-heal playbooks. For example `https://myawx.example.com/api`.
  This variable is mandatory when `openshift_autoheal_deploy` is `true`, it doesn't
  have a default value.

- `openshift_autoheal_awx_proxy`: The URL of the proxy that should be used to
  connect to the Ansible Tower or AWX server. For example
  `http://myproxy.example.com:3128`. Defaults to no proxy.

- `openshift_autoheal_awx_user`: The name of the Ansible Tower or AWX user.
  Defaults to `autoheal`.

- `openshift_autoheal_awx_password`: The password of the Ansible Tower or AWX user.
  This variable is mandatory when `openshift_autoheal_deploy` is `true`, it doesn't
  have a default value.

- `openshift_autoheal_awx_ca`: PEM encoded CA certificates that will be used to
  verify the certificate presented by the Ansible Tower or AWX server. Defaults
  to the CA certificates of the machine.

- `openshift_autoheal_awx_project`: The name of the Ansible Tower or AWX project
  that contains the aut-heal job templates. Defaults to `Auto-heal`.

For example, to install the auto-heal service so that it talks to the AWX server
in `myawx.example.com', add these variables to your inventory file:

```ini
openshift_autoheal_deploy=true
openshift_autoheal_awx_address="https://myawx.example.com/api"
openshift_autoheal_awx_user="myuser"
openshift_autoheal_awx_password="mypassword"
openshift_autoheal_awx_project="MyProject"
```

And then run the following command:

```
$ ansible-playbook -i myinventory.ini playbooks/openshift-autoheal/config.yml
```

# Configuration

The auto-heal service has two main kinds of configuration: the details to
connect to the AWX server and the healing rules.

The details to connect to the AWX server are taken from the variables defined in
the previous section.

The healing rules are taken from the [`rules`](rules) directory inside this role.
Every `.yml` file in that directory should contain exactly one healing rule,
which will be loaded and appended to the configuration file when the service is
installed.

The syntax of the healing rules is described in detail in the documentation of
the auto-heal service, available [here](https://github.com/openshift/autoheal).

To add or modify a healing rule in your development environment create a new
`.yml` file in the [`rules`](rules) directory. For example, to create a rule
that reacts to the alert `MyAlert` executing an AWX job from template
`MyTemplate`, do the following:

```
$ git checkout https://github.com/openshift/openshift-ansible.git
$ cd openshift-ansible
$ cat >> roles/openshift-autoheal/rules/my-rule.yml <<.
metadata:
  name: my-rule
labels:
  alertname: "MyAlert"
awxJob:
  template: "MyTemplate"
.
```

Then install or re-install the auto-heal service:

```
$ ansible-playbook -i myinventory.ini playbooks/openshift-autoheal/config.yml
```

Note that the AWX template, `MyTemplate` in this example, has to exist in the
AWX server in advance, this role does *not* take care of that.

# Requirements

Ansible 2.4.

## License

Apache license, version 2.0.
