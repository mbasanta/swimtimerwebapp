## Ansible Pip playbook [![Build Status](https://travis-ci.org/mbasanta/pip.png)](https://travis-ci.org/mbasanta/pip)

This is a simple Ansible playbook that installs Pip from either source or the
get-pip.py installer.


#### Requirements & Dependencies

##### Ansible

I've tested this on Ansible 1.5.5. I'm not familar enough with features to know
what older versions this is compaible with.


##### Platforms

I've tested this on Ubuntu 14.04 only. I've tried to set it up to work on any
Debian, Fedora, or Suse Linux distro. If you have problems, try installing from
with the installer method instead of the package manager.


#### Variables
Only three simple variables

- `os_family` - Set the OS family [Debian, Fedora, Suse]
- `pip_install_method` - Install with the package installer (package) or the get-pip installer (installer)
- `pip_install_url` - The url for the get-pip.py installer


I'd like to thank Ansibles on GitHub. I've used their playbooks for much of my
inspiration.
- [Ansibles](https://github.com/Ansibles)
