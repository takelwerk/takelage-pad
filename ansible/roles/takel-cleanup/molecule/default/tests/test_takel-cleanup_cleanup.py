import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_cleanup_check_cleanup(host, testvars):
    if testvars['takel_cleanup_enable']:
        absent_files = testvars['takel_cleanup_absent_files']
        for file in absent_files:

            assert not host.file(file).exists
