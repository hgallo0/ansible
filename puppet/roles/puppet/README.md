Role Name
=========

set up a puppet server on Centos 7

Requirements
------------

Role Variables
--------------

JAVA_ARGS: -Xms1g and -Xmx1g

Dependencies
------------

Need to add
-----------

need to add selinux rules
need to add OS identification logic


Example Playbook
----------------

---
- hosts: puppet
  user: root

  roles:
    - puppet

License
-------

HG

Author Information
------------------

Henry Gallo

