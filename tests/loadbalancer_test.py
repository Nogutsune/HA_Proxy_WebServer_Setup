import testinfra
import pytest

#host = testinfra.get_host("ansible://all?ansible_inventory=inventory/hosts")
testinfra_hosts = ["loadbalancer"]

#print host.ansible.get_variables()['inventory_hostname']

@pytest.fixture(scope='module')
def hostname(host):
    return host.ansible.get_variables()['inventory_hostname']

################################# TestCases ###########################################

#TestCase for having root prevelleges
def test_sudo(host):
    with host.sudo():
        assert host.check_output('whoami') == 'root'

#TestCase for validating haproxy is installed on the loadbalancer
def test_haproxy_is_installed(host):
        haproxy = host.package("haproxy")
        assert haproxy.is_installed

#TestCase for validating the haproxy service is running on the loadbalancer
def test_haproxy_services_running_and_enabled(host):
    service = host.service('haproxy')
    assert service.is_running
    assert service.is_enabled

# Testcase for validating loadbalancer is working fine even one node is down
def test_loadbalancer_active_after_one_node_goes_down(host):
    host2 = testinfra.get_host("ansible://192.168.33.20?ansible_inventory=inventory/hosts&force_ansible=True",sudo=True)
    try:
        service_haproxy(host2, 'stop')
        wait_awhile()
        test_loadbalancer()
    finally:
        # After the test, make sure that haproxy is started again
        service_haproxy(host2, 'start')
        wait_awhile()

def service_haproxy(host, state):
    cmd = host.run("sudo service apache2 "+state )
    assert cmd.rc == 0

def wait_awhile():
    import time
    time.sleep(10)

def curl_loadbalancer():
    import subprocess
    return subprocess.call([ "/usr/bin/curl", "-vs",
        "--connect-timeout", "1", "http://192.168.33.30"])

#TestCase for checking curl is working for loadbalancer
def test_loadbalancer():
    assert curl_loadbalancer() == 0
