import pytest
import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


@pytest.mark.parametrize('env, value', [(0, 'DEBIAN_FRONTEND=noninteractive'),
                                        (1, 'LANG=en_US.UTF-8')])
def test_image_meta_env_values(image_meta_data, env, value):
    assert image_meta_data['Config']['Env'][env] == value


def test_image_meta_cmd(image_meta_data):
    assert image_meta_data['Config']['Cmd'] == ["/lib/systemd/systemd"]


def test_image_meta_user(image_meta_data):
    assert image_meta_data['Config']['User'] == ''
