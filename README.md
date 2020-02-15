Ansible role: source-gnucobol
=============================

[![Build Status](https://travis-ci.org/nmusatti/source-gnucobol.svg?branch=master)](https://travis-ci.org/nmusatti/source-gnucobol)

An Ansible role to download and install Gnu COBOL from source. Currently only Red Hat distributions are supported,
i.e. CentOS 7, CentOS 8 and Fedora.

Inspired by the [ansible-role-gnu-cobol](https://github.com/ChristopherDavenport/ansible-role-gnu-cobol) role.

Requirements
------------

None.

Role Variables
--------------

The variables that control the role behaviour are listed below with their respective defaults:

    gnucobol_install_dir: /opt

The base directory of the installation

    gnucobol_release: 3.0

The Gnu COBOL release to install. Currently valid values are: 1.1, 2.0, 2.2 and 3.0.

    gnucobol_user: gnucobol

The owner of the installation.

    gnucobol_group: gnucobol


The installation group.

    gnucobol_src_dir: /sw/gnucobol

The directory where the source archive is downloaded, extracted and built.

    gnucobol_force: false

When `true` installation is performed even if a bug fix release of the same minor version was already installed.
Useful to repeat installations after something went wrong or to perform upgrades.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: nmusatti.source-gnucobol
           vars:
             gnucobol_release: 2.2

License
-------

GPLv3

Author Information
------------------

Nicola Musatti - https://github.com/nmusatti
