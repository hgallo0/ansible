Role Name
=========

Role to spin up ec2 instances in aws

Requirements
------------
boto

Role Variables
--------------
# these can be included in the vars main file
own: account#
key: ssh key
type: type of system, example t2.micro
region: example us-east-1
ami: "ami-yourami" not needed we have a discovery list
tag: tag with key "project"
subnet: subnet-1111111
sg: "sg-11111"
start_seq: integer start seq
end_seq: integer end seq
domain: example.com

Dependencies
------------
keypair.yml file with AWS key information
example below:
# aws personal account
ec2_access_key: "****************"
ec2_secret_key: "************************"


Example Playbook
----------------
---
- name: deploy ec2 instances
  hosts: localhost
  vars_files:
   - keypair.yml

  roles:
  - ec2-nodes

License
-------
none

Author Information
------------------
Henry Gallo


How to run 
-----------------
ansible-playbook spinup_nodes.yml --extra-vars="start_seq=1 end_seq=1" --ask-vault-pass
