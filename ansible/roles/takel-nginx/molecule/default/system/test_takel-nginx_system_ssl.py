import datetime
import pytest
import socket
import takeltest
from cryptography import x509
from cryptography.x509.oid import NameOID
from OpenSSL import SSL

testinfra_hosts = takeltest.hosts()


@pytest.fixture()
def get_remote_ssl_cert(testvars):
    ssl_host = testvars['ansible_hostname']
    sock = socket.socket()
    sock.connect((f"{ssl_host}", 443))
    ctx = SSL.Context(SSL.SSLv23_METHOD)  # most compatible
    ctx.check_hostname = False
    ctx.verify_mode = SSL.VERIFY_NONE

    sock_ssl = SSL.Connection(ctx, sock)
    sock_ssl.set_connect_state()
    sock_ssl.set_tlsext_host_name(ssl_host.encode('utf-8'))
    sock_ssl.do_handshake()
    cert = sock_ssl.get_peer_certificate()
    crypto_cert = cert.to_cryptography()
    sock_ssl.close()
    sock.close()
    return crypto_cert


@pytest.fixture(name='ssl_cert')
def extract_cert_infos(get_remote_ssl_cert):
    cert = {
        'alternative_names': [], 'common_name': '', 'country_name': '',
        'organization_name': '',
        'not_valid_after': get_remote_ssl_cert.not_valid_after,
        'not_valid_before': get_remote_ssl_cert.not_valid_before}

    names = \
        get_remote_ssl_cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
    if names:
        cert['common_name'] = names[0].value

    countries = \
        get_remote_ssl_cert.subject.get_attributes_for_oid(
            NameOID.COUNTRY_NAME)
    if countries:
        cert['country_name'] = countries[0].value

    organizations = \
        get_remote_ssl_cert.subject.get_attributes_for_oid(
            NameOID.ORGANIZATION_NAME)
    if organizations:
        cert['organization_name'] = organizations[0].value

    x509_extansions = \
        get_remote_ssl_cert.extensions.get_extension_for_class(
            x509.SubjectAlternativeName)
    if x509_extansions:
        cert['alternative_names'] = \
            x509_extansions.value.get_values_for_type(x509.DNSName)

    return cert


def test_takel_nginx_system_nginx_cert_url(ssl_cert, testvars):
    nginx_url = testvars['takel_nginx_server_names'][0]
    url_in_common_name = False
    url_in_alternative_names = False
    url_in_common_name_wildcard = False

    if 'common_name' in ssl_cert.keys() and '*.' in ssl_cert['common_name']:
        url_in_common_name_wildcard = True
    if 'common_name' in ssl_cert.keys() and ssl_cert['common_name'] == \
            nginx_url:
        url_in_common_name = True
    if 'alternative_names' in ssl_cert.keys() and \
            nginx_url in ssl_cert['alternative_names']:
        url_in_alternative_names = True

    assert url_in_common_name or \
        url_in_alternative_names or \
        url_in_common_name_wildcard


def test_takel_nginx_system_nginx_cert_not_after(ssl_cert):
    assert ssl_cert['not_valid_after'] > datetime.datetime.utcnow()


def test_takel_nginx_system_nginx_cert_not_before(ssl_cert):
    assert ssl_cert['not_valid_before'] < datetime.datetime.utcnow()
