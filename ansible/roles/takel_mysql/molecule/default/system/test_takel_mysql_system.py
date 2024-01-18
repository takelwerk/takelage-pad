import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_takel_mysql_system_query_mysql_table(host):
    query = "SELECT host FROM mysql.user WHERE user='root'"
    command = f'mysql --batch --skip-column-names --execute="{query}"'
    result = host.check_output(command)

    assert 'localhost' == result
