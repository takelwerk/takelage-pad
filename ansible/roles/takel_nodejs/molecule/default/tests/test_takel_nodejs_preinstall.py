import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_nodejs_preinstall_packages_installed(host, testvars):
    takel_nodejs_deb_preinstall_packages = \
        testvars['takel_nodejs_deb_preinstall_packages']

    for package in takel_nodejs_deb_preinstall_packages:
        deb = host.package(package)

        assert deb.is_installed
