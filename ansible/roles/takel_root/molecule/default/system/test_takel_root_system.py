import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_root_system_includes_alias(host, testvars):
    with host.sudo():
        output = host.check_output('bash -i -c "alias"')
        assert 'alias l=' in output
