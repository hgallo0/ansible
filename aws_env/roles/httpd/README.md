Role Name
=========

Sample loading apache with very very very basic index.html file for demonstration purposes 

Requirements
------------

none

Role Variables
--------------

none 

Dependencies
------------

none

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

---
- name: create LB
  hosts: tag_project_"{{ Project }}" 
  user: ec2-user
  become: yes

  roles:
  - httpd


Author Information
------------------

henry gallo

How to run
-----------------
ansible-playbook loadApache.yml -i ec2.py --private-key=key.pem -e "Project=myproject"
