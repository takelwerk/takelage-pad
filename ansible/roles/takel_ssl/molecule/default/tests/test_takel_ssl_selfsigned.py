import re
import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_ssl_selfsigned_common_name(host, testvars):
    if not ('takel_ssl_cert' in testvars and
            testvars['takel_ssl_cert'] and
            'takel_ssl_key' in testvars and
            testvars['takel_ssl_key']):
        common_name_expected = testvars['takel_ssl_common_name']
        certs_path = testvars['takel_ssl_certs_path']
        cert_file = testvars['takel_ssl_cert_file']
        cert_infos = host.check_output(
            f"openssl x509 "
            f"-in {certs_path}/{cert_file} "
            f"-text")
        common_name = \
            re.search(r'Subject: .* CN = (.*?)[\n|,]', cert_infos)
        if common_name is not None:
            assert common_name.group(1) == common_name_expected
        else:
            assert False


def test_takel_ssl_selfsigned_organization_name(host, testvars):
    if not ('takel_ssl_cert' in testvars and
            testvars['takel_ssl_cert'] and
            'takel_ssl_key' in testvars and
            testvars['takel_ssl_key']):
        expected_organization_name = \
            testvars['takel_ssl_organization_name']
        certs_path = testvars['takel_ssl_certs_path']
        cert_file = testvars['takel_ssl_cert_file']
        cert_infos = host.check_output(
            f"openssl x509 "
            f"-in {certs_path}/{cert_file} "
            f"-text")
        organization_name = \
            re.search(r'Subject: .* O = (.*?)[\n|,]', cert_infos)
        if organization_name is not None:
            assert organization_name.group(1) == expected_organization_name
        else:
            assert False


def test_takel_ssl_selfsigned_subject_alt_name(host, testvars):
    if not ('takel_ssl_cert' in testvars and
            testvars['takel_ssl_cert'] and
            'takel_ssl_key' in testvars and
            testvars['takel_ssl_key']):
        expected_subject_alt_name_list = \
            testvars['takel_ssl_subject_alt_name']
        certs_path = testvars['takel_ssl_certs_path']
        cert_file = testvars['takel_ssl_cert_file']
        cert_infos = host.check_output(
            f"openssl x509 "
            f"-in {certs_path}/{cert_file} "
            f"-text")
        for expected_subject_alt_name in expected_subject_alt_name_list:
            subject_alt_name = \
                re.search(r'DNS:(.*)\n', cert_infos)
            if subject_alt_name is not None:
                assert expected_subject_alt_name in subject_alt_name.group(1)
            else:
                assert False
