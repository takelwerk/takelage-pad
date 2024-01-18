import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_systemd_services_files_exists(host, testvars):
    systemd_services_list = testvars['takel_systemd_service_list']
    for service in systemd_services_list:
        expected_path = f"/etc/systemd/system/{service['name']}.service"
        assert host.file(expected_path).is_file
        assert host.file(expected_path).user == 'root'
        assert host.file(expected_path).group == 'root'
        assert host.file(expected_path).mode == 0o0644
