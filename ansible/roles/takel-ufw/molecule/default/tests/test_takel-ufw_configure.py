import pytest
import re
import takeltest

testinfra_hosts = takeltest.hosts()


@pytest.fixture(name='ufw_default_policies')
def takel_ufw_get_default_policies(host):
    ufw_default_policies = ''
    ufw_status_verbose = host.check_output('ufw status verbose')
    for line in ufw_status_verbose.splitlines():
        if line.startswith('Default: '):
            ufw_default_policies = line
    return ufw_default_policies


@pytest.fixture(name='ufw_rules_numbered')
def takel_ufw_get_numbered_rules(host):
    ufw_rules_numbered = ''
    ufw_numbered_rules = host.check_output('ufw status numbered')
    for line in ufw_numbered_rules.splitlines():
        if line.startswith('['):
            ufw_rules_numbered += line
    return ufw_rules_numbered


def test_takel_ufw_configure_rules_match(testvars, ufw_rules_numbered):
    our_rules = testvars['takel_ufw_rules']

    for our_rule in our_rules:
        expected_rule = \
            rf"{our_rule['port']}/{our_rule['proto']}.*{our_rule['rule']}"

        # assert every one of our rules is active
        assert re.search(
            expected_rule,
            ufw_rules_numbered,
            re.MULTILINE | re.IGNORECASE), \
            'our rule is not active on the server'

    # assert number of ufw rules is not bigger than number of our rules
    assert not re.search(
        rf"\[\s*{len(our_rules) + 1}\]",
        ufw_rules_numbered,
        re.MULTILINE), \
        'there are more rules on the host than we have defined'


def test_takel_ufw_configure_default_policy(testvars, ufw_default_policies):
    policies = testvars['takel_ufw_policies']
    for policy in policies:
        expected_policy = f"{policy['policy']} ({policy['direction']})"

        assert expected_policy in ufw_default_policies
