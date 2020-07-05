import re
import takeltest

testinfra_hosts = takeltest.hosts()


def test_takel_etherpad_system_node_version(host, testvars):
    nodejs_version = str(testvars['takel_etherpad_nodejs_version'])
    nodejs_version_output = host.check_output('node --version')
    nodejs_version_search = re.search(
        r'.*v(\d{1,2})\.\d{0,2}\.\d{0,2}.*', nodejs_version_output)

    if nodejs_version_search is not None:
        assert nodejs_version_search.group(1) == nodejs_version
    else:
        assert False, 'Unable to get nodejs version'
