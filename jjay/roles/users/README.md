Role Name
=========

small playbook to add or delete users 

Requirements
------------

none

Role Variables
--------------

users should be define in the vars main file as follow:

users:
  - camou.gallo
  - kalamaras.gallo
  - charles.gallo
  - saliaga.gallo
  - acurcio.gallo

password should be define as:

password: $6$liMcyI...........................

Dependencies
------------


Example Playbook
----------------

---
- name: adding/removing users
  hosts: servers
  user: username
  become: yes

  roles:
  - users

##### CAUTION ##### 
Beware of the tags 
sample run to add users
  ansible-playbook users.yml -i hosts --tags add
sample run to delete users
  ansible-playbook users.yml -i hosts --tags remove

Author Information
------------------
Henry Gallo

