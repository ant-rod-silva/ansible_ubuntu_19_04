Introduction
=========

OpenLDAP is Open Source alternative to Microsoft Active Directory. 
LDAP (Lightweight Directory Access Protocol) is used to manage related information from a centralized location through the use of a file and directory hierarchy.


Requirements
------------

- Ansible >= 2.7
- Python

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).

Answers
------------------

- Omit OpenLDAP server configuration? No
- DNS domain name?
This option will determine the base structure of your directory path. Read the message to understand exactly how this will be implemented. You can actually select whatever value you'd like, even if you don't own the actual domain. However, this tutorial assumes you have a proper domain name for the server, so you should use that. We'll use example.com throughout the tutorial.
- Organization name?
For this guide, we will be using example as the name of our organization. You may choose anything you feel is appropriate.
Administrator password? enter a secure password twice
- Database backend? MDB
- Remove the database when slapd is purged? No
- Move old database? Yes
- Allow LDAPv2 protocol? No

## References

https://www.cyrill-gremaud.ch/how-to-add-new-schema-to-openldap-2-4/
https://docs.secureauth.com/display/KBA/Active+Directory+Attributes+List
https://www.userbooster.de/en/support/feature-articles/feature-article146.aspx
https://github.com/dkoudela/active-directory-to-openldap/tree/master/schema
