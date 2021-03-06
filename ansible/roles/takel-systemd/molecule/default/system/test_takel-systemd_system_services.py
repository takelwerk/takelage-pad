import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_systemd_services_service_enabled(host, testvars):
    systemd_services_list = testvars['takel_systemd_service_list']
    systemd_service_enabled = \
        host.check_output('systemctl list-unit-files | grep enabled')
    for service in systemd_services_list:
        assert service['name'] in systemd_service_enabled


# def test_takel_systemd_services_service_running(host, testvars):
#     systemd_services_list = testvars['takel_systemd_service_list']
#     for service in systemd_services_list:
#         assert host.service(service['name'] + '.service').is_running


def test_takel_systemd_services_service_running(host, testvars):
    systemd_services_list = testvars['takel_systemd_service_list']
    systemd_service_enabled = \
        host.check_output('systemctl list-unit-files | grep enabled')
    for service in systemd_services_list:
        assert service['name'] in systemd_service_enabled
