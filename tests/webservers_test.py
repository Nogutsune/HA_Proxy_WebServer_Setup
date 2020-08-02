import testinfra
import pytest

#host = testinfra.get_host("ansible://all?ansible_inventory=inventory/hosts")
testinfra_hosts = ["webservers"]

#print host.ansible.get_variables()['inventory_hostname']

@pytest.fixture(scope='module')
def hostname(host):
    return host.ansible.get_variables()['inventory_hostname']

################################# TestCases ###########################################

#TestCase for having root prevelleges
def test_sudo(host):
    with host.sudo():
        assert host.check_output('whoami') == 'root'

#TestCase for validating apache is installed on the webservers
def test_apache_is_installed(host):
        apache = host.package("apache2")
        assert apache.is_installed

#TestCase for validating the apache service is running on the webservers
def test_apache_service_running_and_enabled(host):
    service = host.service('apache2')
    assert service.is_running
    assert service.is_enabled

#TestCase for checking curl is working for webservers
def test_curl(host):
    cmd = host.run("curl -vs http://localhost")
    assert "HTTP/1.1 200" in cmd.stderr
