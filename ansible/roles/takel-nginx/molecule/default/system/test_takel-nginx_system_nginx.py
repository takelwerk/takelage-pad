import ssl
import takeltest
import urllib.request

testinfra_hosts = takeltest.hosts()


def test_takel_nginx_system_nginx_service_enabled(host):
    assert host.service('nginx').is_enabled


def test_takel_nginx_system_nginx_service_running(host):
    assert host.service('nginx').is_running


def test_takel_nginx_system_nginx_http(testvars):
    nginx_host = testvars['ansible_hostname']
    valid_return_codes = [
        '200',
        'HTTP/1.1 301 Moved Permanently'
    ]
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    try:
        page = urllib.request.urlopen(
            f"http://{nginx_host}",
            context=context)
        assert str(page.getcode()) in valid_return_codes
    except urllib.error.HTTPError as e:
        if e.code == 401:
            assert True, \
                "Server error 401 probably means that " \
                "basic auth blocked access"
            return
        else:
            assert False, \
                "The server couldn't fulfill the request. " \
                f"Error code: {e.code}"
    except urllib.error.URLError as e:
        assert False, \
            'We failed to reach a server. ' \
            f"Reason: {e.reason}"


def test_takel_nginx_system_nginx_https(testvars):
    nginx_host = testvars['ansible_hostname']
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    try:
        page = urllib.request.urlopen(
            f"https://{nginx_host}/",
            context=context)
        assert 200 == page.getcode()
    except urllib.error.HTTPError as e:
        if e.code == 401:
            assert True, \
                "Server error 401 probably means that " \
                "basic auth blocked access"
            return
        else:
            assert False, \
                "The server couldn't fulfill the request. " \
                f"Error code: {e.code}"
    except urllib.error.URLError as e:
        assert False, \
            'We failed to reach a server. ' \
            f"Reason: {e.reason}"
