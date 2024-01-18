import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ssl_casigned_ssl_key_content(host, testvars):
    if ('takel_ssl_cert' in testvars and
            testvars['takel_ssl_cert'] and
            'takel_ssl_key' in testvars and
            testvars['takel_ssl_key']):

        key_path = testvars['takel_ssl_key_path']
        key_file = testvars['takel_ssl_key_file']

        key = host.file(key_path + '/' + key_file)

        assert key.content_string.strip() == testvars['takel_ssl_key']


def test_takel_ssl_casigned_ssl_cert_content(host, testvars):
    if ('takel_ssl_cert' in testvars and
            testvars['takel_ssl_cert'] and
            'takel_ssl_key' in testvars and
            testvars['takel_ssl_key']):

        certs_path = testvars['takel_ssl_certs_path']
        cert_file = testvars['takel_ssl_cert_file']

        cert = host.file(certs_path + '/' + cert_file)

        cert_chain = testvars['takel_ssl_cert']

        if 'takel_ssl_ca' in testvars and testvars['takel_ssl_ca']:
            cert_chain += '\n' + testvars['takel_ssl_ca']

        assert cert.content_string.strip() == cert_chain
