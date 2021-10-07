import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_nodejs_bash_completion(host, testvars):
    completion_file = testvars['takel_nodejs_bash_completion']
    file = host.file(completion_file)

    assert file.exists
    assert file.is_file
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o644
