# frozen_string_literal: true

@cmd_test_all_roles = 'for dir in ' \
    '`find ansible/roles -maxdepth 2 -name molecule | sort`; ' \
    'do ' \
    'cd `dirname $dir`; ' \
    'molecule test; ' \
    'cd ../../../; ' \
    'done'

@cmd_ansible_role = "'cd %<role_path>s && " \
                    "molecule %<command>s'"

@list_ansible_role = %i[converge destroy login test verify]
