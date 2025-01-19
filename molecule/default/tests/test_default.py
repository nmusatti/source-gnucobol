import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_cobc(host):
    f = host.file('/opt/gnucobol-3.2/bin/cobc')
    assert f.exists
    assert f.user == 'gnucobol'
    assert f.group == 'gnucobol'

    assert '3.2' in host.check_output(
        '/opt/gnucobol-3.2/bin/cobc --version')
