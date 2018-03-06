# Auto-heal playbooks

This directory contains a set of playbooks useful for preparing the
auto-heal environment.

To use them create an inventory file like this:

```ini
[oo_first_master]
master.example.com

[nodes]
master.example.com
node0.example.com
node1.example.com

[all:vars]
openshift_autoheal_awx_host = myawx.example.com
openshift_autoheal_awx_admin_password = ...
openshift_autoheal_awx_user_password = ...
```

The `admin` password should be the password of the AWX administrator
user that will be used to create all the relevant objects (the auto-heal
organization, the auto-heal project, the auto-heal user, etc).

The `user` password is the password that will be assigned to the
`autoheal` user that will be created. This is the user that will be used
to launch the auto-heal jobs.

These are the available playbooks, in the order that you will want to
execute them:

- `install_autoheal_service.yml`: Creates the auto-heal namespace and
  creates all the Kubernetes objects needed by the auto-heal service.

- `generate_ssh_keypair.yml`: Generates a new SSH key pair and stores it
  in the `.ssh` directory, in the `id_autoheal` and `id_autoheal.pub`
  files, and copies it to the `authorized_keys` files of all the nodes
  of the cluster.

- `install_awx_cli.yml`: Installs in the local host the AWX CLI.

- `prepare_awx_server.yml`: Prepares the AWX server, creating all the
  required objects.

- `create_example_template.yml`: Creates an example job template with
  a simple playbook that starts the API server.
