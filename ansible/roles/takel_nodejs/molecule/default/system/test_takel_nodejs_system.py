from packaging import version
import re
import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_nodejs_system_node_available(host, testvars):
    nodejs_version_expected = testvars['takel_nodejs_repository_version']
    nodejs_version_output = host.check_output('node --version')

    nodejs_version_search = re.search(
        r'v(\d{1,2}\.\d{1,2}\.?\d{1,2}?).*',
        nodejs_version_output)

    if nodejs_version_search is not None:
        assert version.parse(nodejs_version_search.group(1)).major == \
               nodejs_version_expected
    else:
        assert False, 'Unable to get node version'


def test_takel_nodejs_system_npm_available(host, testvars):
    npm_version_output = host.check_output('npm --version')

    if npm_version_output is not None:
        assert version.Version(npm_version_output)
    else:
        assert False, 'Unable to get npm version'
