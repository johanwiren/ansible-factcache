ansible-factcache
=================

A callback plugin and a custom inventory script used to store and fetch ansible fact data in Redis.

Requirements
-------------

* A running redis instance

Installation
------------

* Copy *inventory.py* to *lib/ansible/callback_plugins*
* Copy *facts_to_groups.py* to */etc/ansible/hosts/* or just use it as your inventory script.

Usage
-----

When installed, run ``ansible -m setup all`` to collect all facts to the cache. When the cache is populated, you can start doing some interesting ad-hoc commands:

    ansible -m shell -a "yum -y upgrade" ansible_os_family_RedHat:&ansible_distribution_version_6.0

Or use them in your playbooks:

    - hosts: ansible_system_OpenBSD
      tasks: 
        - debug: msg="Wow, this machine is awesome"

Bugs
----

Only simple facts are stored, no hashes or lists.


