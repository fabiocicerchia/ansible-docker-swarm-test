import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('keyfile,certfile', [
    ('/root/.docker/server-key.pem', '/root/.docker/server-cert.pem'),
])
def test_certificates_are_valid(host, keyfile, certfile):
    cmd = 'openssl rsa -in ' + keyfile + ' -check'
    with host.sudo():
        assert host.check_output(cmd) == 'root'

    cmd = 'openssl x509 -in ' + certfile + ' -text -noout'
    with host.sudo():
        assert host.check_output(cmd) == 'root'


def test_docker_is_installed(host):
    docker = host.package('docker')
    assert docker.is_installed
    assert docker.version == '2'


def test_docker_running_and_enabled(host):
    docker = host.service('docker')
    assert docker.is_running
    assert docker.is_enabled


def test_docker_api_is_listening(host):
    socket = host.socket('tcp://0.0.0.0:2375')
    assert socket.is_listening
