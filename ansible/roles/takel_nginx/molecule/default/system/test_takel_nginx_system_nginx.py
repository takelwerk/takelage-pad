import takeltest

# web server
testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_nginx_system_nginx_service_enabled(host):
    assert host.service('nginx').is_enabled


def test_takel_nginx_system_nginx_service_running(host):
    assert host.service('nginx').is_running
