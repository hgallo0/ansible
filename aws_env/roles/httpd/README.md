Role Name
=========

<<<<<<< HEAD
Sample loading apache with very very very basic index.html file for demonstration purposes 
=======
A brief description of the role goes here.
>>>>>>> secGroups

Requirements
------------

<<<<<<< HEAD
none
=======
Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.
>>>>>>> secGroups

Role Variables
--------------

<<<<<<< HEAD
none 
=======
A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.
>>>>>>> secGroups

Dependencies
------------

<<<<<<< HEAD
none
=======
A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.
>>>>>>> secGroups

Example Playbook
----------------

<<<<<<< HEAD
Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

---
- name: create LB
  hosts: tag_project_"{{ Project }}" 
=======
---
- name: installing apache
  hosts: tag_Name_server_1_henry_com
>>>>>>> secGroups
  user: ec2-user
  become: yes

  roles:
  - httpd
<<<<<<< HEAD

=======
#  - mysql

License
-------

BSD
>>>>>>> secGroups

Author Information
------------------

<<<<<<< HEAD
henry gallo

How to run
-----------------
ansible-playbook loadApache.yml -i ec2.py --private-key=key.pem -e "Project=myproject"
=======
An optional section for the role authors to include contact information, or a website (HTML is not allowed).

How to run
-----------------
ansible-playbook -i ec2.py apache.yml --private-key=shu.pem
>>>>>>> secGroups
