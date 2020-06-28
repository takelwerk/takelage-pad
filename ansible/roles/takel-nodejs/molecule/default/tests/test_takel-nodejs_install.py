import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_nodejs_install_deb_prerequisites_installed(host, testvars):
    install_prerequisites = testvars['takel_nodejs_deb_install_prerequisites']

    for install_prerequisite in install_prerequisites:
        prerequisite = host.package(install_prerequisite)

        assert prerequisite.is_installed


def test_takel_nodejs_install_deb_packages_installed(host, testvars):
    install_packages = testvars['takel_nodejs_deb_install_packages']

    for install_package in install_packages:
        package = host.package(install_package)

        assert package.is_installed
