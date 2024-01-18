import takeltest

# system test server
testinfra_hosts = [f"{takeltest.hosts()[0]}-system"]


def test_takel_nginx_system_web_http(host, testvars):
    ip = testvars['ansible_all_ipv4_addresses'][0]
    curl_command = "curl -o /dev/null --silent --head --write-out '%{http_code}\n'"
    http_code = host.check_output(f"{curl_command} {ip}")
    valid_return_codes = [
        '200',
        '301'
    ]
    assert http_code in valid_return_codes


def test_takel_nginx_system_nginx_https(host, testvars):
    ip = testvars['ansible_all_ipv4_addresses'][0]
    curl_command = "curl -o /dev/null --silent --head --write-out '%{http_code}\n'"
    http_code = host.check_output(f"{curl_command} {ip}")
    valid_return_codes = [
        '200',
        '301'
    ]
    assert http_code in valid_return_codes
