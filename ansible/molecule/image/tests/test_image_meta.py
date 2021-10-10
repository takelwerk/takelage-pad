import takeltest
import os
import pytest

testinfra_hosts = [takeltest.hosts()[0]]


def test_image_meta_env_exists(image_meta_data):
    assert image_meta_data['Config']['Env'] is not None


def test_image_meta_cmd(testvars, image_meta_data):
    image = os.environ.get('TAKELAGE_PROJECT_IMG')
    if 'command' in testvars['project']['images'][image]:
        expected = ['/bin/sh', '-c'] + \
                   testvars['project']['images'][image]['command'].split(' ')
    else:
        expected = ['/bin/sh', '-c', '/usr/bin/tail -f /dev/null']
    assert expected == image_meta_data['Config']['Cmd']


def test_image_meta_user(image_meta_data):
    assert image_meta_data['Config']['User'] == ''


@pytest.mark.parametrize('process, expected_args', [
    ('systemd',    '/lib/systemd/systemd')])
def test_container_process(host, process, expected_args):
    procs_present = False
    process_result = host.process.filter(user='root', comm=process)
    for proc in process_result:
        if proc.args == expected_args:
            procs_present = True
            break

    assert procs_present is True
