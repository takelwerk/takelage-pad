import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ssl_configure_create_folders(host, testvars):
    certs_path = host.file(testvars['takel_ssl_certs_path'])
    key_path = host.file(testvars['takel_ssl_key_path'])

    for path in [certs_path, key_path]:
        assert path.exists
        assert path.is_directory
