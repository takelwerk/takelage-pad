import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_takelpad_version_file(host, testvars):
    if 'takel_takelpad_version' in testvars:
        version = testvars['takel_takelpad_version']
        file = host.file('/etc/takelpad_version')

        assert file.exists
        assert file.is_file
        assert file.user == 'root'
        assert file.group == 'root'
        assert file.mode == 0o644
        assert version == file.content_string
