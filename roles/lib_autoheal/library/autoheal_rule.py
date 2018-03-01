#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (c) 2018 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': [
        'preview',
    ],
    'supported_by': 'community',
}


DOCUMENTATION = '''
---
module: autoheal_rule
short_description: Module to manage auto-heal rules.
version_added: "2.4"
description:
- "Module to manage auto-heal rules"

options:
  name:
    description:
    - "The name of the auto-heal rule"
    required: true
  state:
    description:
    - "Should the rule be present or absent"
    choices: ['absent', 'present']
    default: present
  conditions:
    description:
    - "List of conditions that the alert should satisfy to activate the rule."
  actions:
    description:
    - "List of actions that will be executed when the rule is activated."
'''

EXAMPLES = '''
# Create an auto-heal rule that is activated for all alerts whose name
# starts with 'NodeDown-' and that runs an AWX job:

autoheal_rule:
  name: start-node
  conditions:
  - alert: "^NodeDown-.*$"
  actions:
  - awxJob:
      address: https://my-awx.example.com
      secretRef:
        name: my-awx-credentials
      project: "My AWX project"
      template: "My AWX template"
      ...

# Create an auto-heal rule that is activated for all alerts whose name
# starts with 'APIServerDown-' and that runs an Ansible Playbook:

autoheal_rule:
  name: start-api-server
  conditions:
  - alert: "^APIServerDown-.*$"
  actions:
  - ansiblePlaybook:
      playbook |-
        ---
        - name: Start API
          hosts: localhost
          connection: local
          gather_facts: false
          tasks:
          ....
'''

from ansible.module_utils.basic import *


def main():
    # Define the available module arguments:
    module_args = dict(
        name=dict(
            default=None,
            required=True,
        ),
        state=dict(
            choices=[
                'absent',
                'present',
            ],
            default='present',
        ),
        conditions=dict(
            default=None,
        ),
        actions=dict(
            type='list',
            default=None,
        ),
    )

    # Seed the result:
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # Create the instance:
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Exit now if in check mode:
    if module.check_mode:
        return result

    # Currently this does nothing, but in the future it will take the
    # description of the healing rule and make sure that it is available for the
    # auto-heal service. That may mean creating an instance of a `HealingRule`
    # Kubernetes object, crating a YAML configuration file, or any other
    # mechanism that is used to configure the auto-heal service.
    module.exit_json(**result)


if __name__ == '__main__':
    main()
