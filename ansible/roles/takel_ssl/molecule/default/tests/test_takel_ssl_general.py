from datetime import datetime
import pytest
import re
import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ssl_general_ssl_key_exists(host, testvars):
    key_path = testvars['takel_ssl_key_path']
    key_file = testvars['takel_ssl_key_file']

    key = host.file(key_path + '/' + key_file)

    assert key.exists
    assert key.is_file

    if ('takel_ssl_cert' in testvars and
            testvars['takel_ssl_cert'] and
            'takel_ssl_key' in testvars and
            testvars['takel_ssl_key']):
        assert key.content_string.strip() == testvars['takel_ssl_key']


def test_takel_ssl_general_ssl_cert_exists(host, testvars):
    certs_path = testvars['takel_ssl_certs_path']
    cert_file = testvars['takel_ssl_cert_file']

    cert = host.file(certs_path + '/' + cert_file)

    assert cert.exists
    assert cert.is_file

    if ('takel_ssl_cert' in testvars and
            testvars['takel_ssl_cert'] and
            'takel_ssl_key' in testvars and
            testvars['takel_ssl_key']):
        if 'takel_ssl_ca' in testvars and testvars['takel_ssl_ca']:
            cert_chain = \
                testvars['takel_ssl_cert'] + '\n' + testvars['takel_ssl_ca']

        assert cert.content_string.strip() == cert_chain


@pytest.fixture()
def test_takel_ssl_get_cert_infos(host, testvars):
    certs_path = testvars['takel_ssl_certs_path']
    cert_file = testvars['takel_ssl_cert_file']
    return host.check_output(
        'openssl x509 '
        '-in ' + certs_path + '/' + cert_file + ' '
        '-text '
        '-noout')


def test_takel_ssl_subject(testvars, test_takel_ssl_get_cert_infos):
    subject = \
        re.search(r'Subject:.*?CN = (.*?)\n', test_takel_ssl_get_cert_infos)
    if subject is not None:
        assert subject.group(1) == testvars['takel_ssl_common_name']
    else:
        assert False


def test_takel_ssl_expire_date(testvars, test_takel_ssl_get_cert_infos):
    expiry_date = \
        re.search(r'Not After : (.*?)\n', test_takel_ssl_get_cert_infos)
    if expiry_date is not None:
        ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
        expiry_datetime = datetime.strptime(expiry_date.group(1), ssl_date_fmt)
        valid_seconds = (expiry_datetime - datetime.now()).total_seconds()
        assert float(testvars['takel_ssl_minimum_valid_seconds']) \
               < valid_seconds
    else:
        assert False
