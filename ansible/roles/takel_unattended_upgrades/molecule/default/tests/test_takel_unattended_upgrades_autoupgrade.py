import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_unattended_upgrades_autoupgrade_20auto_upgrades(host, testvars):
    autoupgrade = testvars['takel_unattended_upgrades_autoupgrade']
    if autoupgrade:
        file = host.file('/etc/apt/apt.conf.d/20auto-upgrades')

        assert file.exists
        assert file.is_file
        assert file.user == 'root'
        assert file.group == 'root'
        assert file.mode == 0o644


def test_takel_unattended_upgrades_autoupgrade_50unattended_upgrades(host,
                                                                     testvars):
    autoupgrade = testvars['takel_unattended_upgrades_autoupgrade']
    if autoupgrade:
        file = host.file('/etc/apt/apt.conf.d/50unattended-upgrades')

        assert file.exists
        assert file.is_file
        assert file.user == 'root'
        assert file.group == 'root'
        assert file.mode == 0o644


def test_takel_unattended_upgrades_autoupgrade__installed(host, testvars):
    autoupgrade = testvars['takel_unattended_upgrades_autoupgrade']
    if autoupgrade:
        package = host.package('unattended-upgrades')

        assert package.is_installed
