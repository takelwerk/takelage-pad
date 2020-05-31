import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_base_version_file(host, testvars):
    version = testvars['takel_base_version']

    file = host.file('/etc/takelage_version')

    assert file.exists
    assert file.is_file
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o644
    assert file.content_string == version + "\n"
