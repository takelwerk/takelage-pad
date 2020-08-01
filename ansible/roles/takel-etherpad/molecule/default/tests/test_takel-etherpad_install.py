import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_etherpad_install_deb_packages_installed(host, testvars):
    install_packages = testvars['takel_etherpad_deb_install_packages']

    for install_package in install_packages:
        package = host.package(install_package)

        assert package.is_installed
