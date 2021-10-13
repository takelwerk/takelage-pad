import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_systemd_services_service_enabled(host, testvars):
    systemd_services_list = testvars['takel_systemd_service_list']
    systemd_service_enabled = \
        host.check_output('systemctl list-unit-files | grep enabled')
    for service in systemd_services_list:
        assert service['name'] in systemd_service_enabled


def test_takel_systemd_services_service_running(host, testvars):
    assert host.service('example-service.service').is_running


def test_takel_systemd_services_service_triggered(host, testvars):
    log = host.check_output('journalctl -u example-service-timer')
    assert 'example-service-timer.service: Succeeded.' in log
