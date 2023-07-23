import re
import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_gopass_system_gopass_available(host):
    gopass_version_output = host.check_output('gopass --version')

    # grep the gopass version
    gopass_version_search = re.search(
        r'gopass\ (\d{1,2}\.\d{1,2}\.?\d{1,2}?).*',
        gopass_version_output)

    assert gopass_version_search is not None, 'Unable to get gopass version'
