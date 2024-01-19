import calendar
import pytest
import re
import time
import takeltest

# system test server
testinfra_hosts = [f"{takeltest.hosts()[0]}-system"]


@pytest.fixture()
def ssl_cert(host, testvars):
    ip = testvars['ansible_all_ipv4_addresses'][0]
    openssl_command = f"</dev/null openssl s_client -connect {ip}:443"
    cert = host.check_output(openssl_command)
    return cert


def test_takel_nginx_system_nginx_cert_url(ssl_cert, testvars):
    nginx_url = testvars['takel_nginx_server_names'][0]
    assert f"CN = {nginx_url}" in ssl_cert


def test_takel_nginx_system_nginx_cert_not_before(ssl_cert):
    not_valid_before = re.search(
        r'.*NotBefore: (.*) GMT;.*',
        ssl_cert,
        flags=re.DOTALL
    ).group(1)
    not_valid_before_struct_time = time.strptime(
        not_valid_before, "%b %d %H:%M:%S %Y")
    not_valid_before_timestamp = calendar.timegm(
        not_valid_before_struct_time)
    assert not_valid_before_timestamp < time.time()


def test_takel_nginx_system_nginx_cert_not_after(ssl_cert):
    not_valid_after = re.search(
        r'.*NotAfter: (.*) GMT.*',
        ssl_cert,
        flags=re.DOTALL
    ).group(1)
    not_valid_after_struct_time = time.strptime(
        not_valid_after, "%b %d %H:%M:%S %Y")
    not_valid_after_timestamp = calendar.timegm(
        not_valid_after_struct_time)
    assert not_valid_after_timestamp > time.time()
