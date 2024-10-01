import docker
import os
import pytest


@pytest.fixture(scope='module')
def docker_client():
    if 'DOCKER_HOST' in os.environ:
        return docker.from_env()
    else:
        docker_sock = 'unix://var/run/docker.sock'
        return docker.DockerClient(base_url=docker_sock)


@pytest.fixture()
def image_meta_data(docker_client, testvars):
    image_meta = docker_client.api.inspect_image(
        testvars['molecule_yml']['platforms'][0]['image'])
    return image_meta
