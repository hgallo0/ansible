ELB
=========

adding elastic load balancer to aws, including ec2-nodes

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

name: name of the load balancer
inst_ids:  [ 'array', 'of', 'ec2-nodes' ]
reg: region example us-east-1
sub: subnet
lb_port: load balancer listening port
inst_port: instance listening port

keypair.yml file
# aws personal account
ec2_access_key: "****************"
ec2_secret_key: "*********************"


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

---
- name: create LB
  hosts: localhost

  vars_files:
    - keypair.yml

  roles:
    - LB

known bugs
------------------

 str(backend.instance_port) + ':' + policy.policy_name for backend in self.elb.backends\nTypeError: 'NoneType' object is not iterable\n"

 https://github.com/ansible/ansible-modules-core/pull/3124/files

Author Information
------------------

Henry Gallo, linuxexamples.org
