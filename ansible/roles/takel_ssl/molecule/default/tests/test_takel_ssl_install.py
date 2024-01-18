import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ssl_install_deb_packages_installed(host, testvars):
    install_packages = testvars['takel_ssl_deb_install_packages']

    for install_package in install_packages:
        package = host.package(install_package)

        assert package.is_installed
