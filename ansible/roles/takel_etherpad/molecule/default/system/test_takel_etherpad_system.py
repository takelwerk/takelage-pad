import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_etherpad_system_curl_etherpad(host, testvars):
    address = 'http://127.0.0.1'
    port = testvars['takel_etherpad_port']
    command = f"curl {address}:{port}"
    result = host.check_output(command)

    assert '<title>Etherpad</title>' in result
