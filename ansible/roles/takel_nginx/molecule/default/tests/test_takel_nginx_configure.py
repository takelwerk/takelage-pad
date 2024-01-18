import pytest
import re
import takeltest

# web server
testinfra_hosts = [takeltest.hosts()[0]]


@pytest.fixture(name='site_config')
def get_site_config(host, testvars):
    site_config = {'http': '', 'https': ''}
    nginx_config_path = testvars['takel_nginx_config_path']
    nginx_config_site_name = testvars['takel_nginx_site_name']
    site_config_path = \
        f"{nginx_config_path}/sites-available/{nginx_config_site_name}"
    site_config_string = \
        host.file(site_config_path).content.decode('utf-8')
    server_http = re.match(
        r'.*server {(.*?listen 80.*?;(?:[\s]*?))}.*',
        site_config_string,
        flags=re.DOTALL
    )
    if server_http:
        site_config['http'] = server_http.group(1)
    server_https = re.match(
        r'.*server {(.*?listen 443.*?;(?:[\s]*?))}.*',
        site_config_string,
        flags=re.DOTALL
    )
    if server_https:
        site_config['https'] = server_https.group(1)
    return site_config


@pytest.mark.parametrize("protocol", ['http', 'https'])
def test_takel_nginx_config_server_name(
        site_config,
        testvars,
        protocol):
    nginx_server_names = testvars['takel_nginx_server_names']
    if 'server_name _;' not in site_config[protocol]:
        for server_name in nginx_server_names:
            assert server_name in site_config[protocol]


def test_takel_nginx_config_ssl_cert(site_config, testvars):
    nginx_ssl_cert = testvars['takel_nginx_ssl_cert']
    config_ssl_cert = re.search(
        r'ssl_certificate (.*);',
        site_config['https']
    )
    if config_ssl_cert is not None:
        assert config_ssl_cert.group(1) == nginx_ssl_cert
    else:
        assert False


def test_takel_nginx_config_ssl_key(site_config, testvars):
    nginx_ssl_key = \
        testvars['takel_nginx_ssl_key']
    config_ssl_key = \
        re.search(r'ssl_certificate_key (.*);', site_config['https'])
    if config_ssl_key is not None:
        assert config_ssl_key.group(1) == nginx_ssl_key
    else:
        assert False


def test_takel_nginx_config_ssl_ciphers(site_config, testvars):
    nginx_ssl_ciphers = \
        testvars['takel_nginx_ssl_ciphers']
    config_ssl_ciphers = \
        re.search(r'ssl_ciphers (.*);', site_config['https'])
    if config_ssl_ciphers is not None:
        assert config_ssl_ciphers.group(1) == ':'.join(nginx_ssl_ciphers)
    else:
        assert False


def test_takel_nginx_config_ssl_session_cache(site_config, testvars):
    nginx_ssl_session_cache = \
        testvars['takel_nginx_ssl_session_cache']
    config_ssl_session_cache = \
        re.search(r'ssl_session_cache (.*);', site_config['https'])
    if config_ssl_session_cache is not None:
        assert config_ssl_session_cache.group(1) == nginx_ssl_session_cache
    else:
        assert False


def test_takel_nginx_site_available(host, testvars):
    nginx_config_path = testvars['takel_nginx_config_path']
    nginx_config_site_name = testvars['takel_nginx_site_name']
    config_file_path = \
        f"{nginx_config_path}/sites-available/{nginx_config_site_name}"
    config_file = host.file(config_file_path)
    assert config_file.exists
    assert config_file.is_file


def test_takel_nginx_site_enabled(host, testvars):
    nginx_config_path = testvars['takel_nginx_config_path']
    nginx_config_site_name = testvars['takel_nginx_site_name']
    config_file_path = \
        f"{nginx_config_path}/sites-enabled/{nginx_config_site_name}"
    config_file = host.file(config_file_path)
    assert config_file.exists
    assert config_file.is_symlink
