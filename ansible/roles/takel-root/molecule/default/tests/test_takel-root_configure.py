import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_root_configure_vimrc(host):
    assert 'syntax on' in host.file('/root/.vimrc').content_string
    assert 'set number' in host.file('/root/.vimrc').content_string
