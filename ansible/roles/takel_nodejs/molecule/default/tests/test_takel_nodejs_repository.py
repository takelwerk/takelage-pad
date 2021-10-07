import takeltest
import re

testinfra_hosts = takeltest.hosts()


def test_takel_nodejs_repository_apt_repository_key(host, testvars):
    key = testvars['takel_nodejs_repository_key']
    command = f"apt-key adv --fetch-keys {key}"
    gpg_result = host.run(command)

    assert gpg_result.rc == 0

    if re.search(r'unchanged: 1', gpg_result.stderr):
        assert True
    else:
        assert False


def test_takel_nodejs_repository_apt_repository(host, testvars):
    nodejs_repository = testvars['takel_nodejs_repository']
    repository_filename = testvars['takel_nodejs_repository_filename']
    file = f"/etc/apt/sources.list.d/{repository_filename}.list"
    sources_list = host.file(file)

    assert nodejs_repository == sources_list.content_string
