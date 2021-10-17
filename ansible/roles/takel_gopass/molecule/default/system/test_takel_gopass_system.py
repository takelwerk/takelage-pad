from packaging import version
import re
import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_gopass_system_gopass_available(host, testvars):
    gopass_version_expected = version.parse(testvars['takel_gopass_version'])
    gopass_version_output = host.check_output('gopass --version')

    # grep the gopass version
    gopass_version_search = re.search(
        r'gopass\ (\d{1,2}\.\d{1,2}\.?\d{1,2}?).*',
        gopass_version_output)

    if gopass_version_search is not None:
        assert version.parse(gopass_version_search.group(1)) == \
               gopass_version_expected
    else:
        assert False, 'Unable to get gopass version'
