Ansible role: source_gnucobol
=============================

![test](https://github.com/nmusatti/source-gnucobol/actions/workflows/test.yml/badge.svg)

An Ansible role to download and install [GnuCOBOL](https://sourceforge.net/projects/gnucobol/)
from source. Supported distributions are the currently maintained releases of
the Red Hat family and derivatives, and Ubuntu. At this time tests are run on
Rocky Linux 9, Rocky Linux 8, CentOS Stream 9, CentOS Stream 8, CentOS 7,
Fedora 36, Fedora 35, Ubuntu 22.04, Ubuntu 20.04 and Ubuntu 18.04.

Inspired by the [ansible-role-gnu-cobol](https://github.com/ChristopherDavenport/ansible-role-gnu-cobol) role.

Requirements
------------

None.

Role Variables
--------------

The variables that control the role behaviour are listed below with their respective defaults:

    gnucobol_install_dir: /opt

The base directory of the installation

    gnucobol_release: 3.1

The Gnu COBOL release to install. Currently valid values are: 1.1, 2.0, 2.2, 3.0 and 3.1.

    gnucobol_user: gnucobol

The owner of the installation.

    gnucobol_group: gnucobol


The installation group.

    gnucobol_src_dir: /sw/gnucobol

The directory where the source archive is downloaded, extracted and built.

    gnucobol_force: false

When `true` installation is performed even if a bug fix release of the same
minor version was already installed. Useful to repeat installations after
something went wrong or to perform upgrades.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: nmusatti.source_gnucobol
           vars:
             gnucobol_release: 3.1

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - https://github.com/nmusatti
