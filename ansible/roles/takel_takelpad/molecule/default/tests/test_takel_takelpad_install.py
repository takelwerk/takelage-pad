import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_takelpad_install_deb_packages_installed(host, testvars):
    install_packages = testvars['takel_takelpad_deb_install_packages']

    for install_package in install_packages:
        package = host.package(install_package)

        assert package.is_installed
