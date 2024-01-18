import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_base_configure_locales(host, testvars):
    file = host.file('/etc/default/locale')
    locales = testvars['takel_base_locales']

    assert file.exists
    assert file.is_file
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o644

    for locale in locales:
        assert locale in file.content_string
