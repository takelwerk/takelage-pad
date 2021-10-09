import pytest
import docker

image_name = 'takelwerk/takelage'
image_tag = 'testing'


@pytest.fixture(scope='module')
def docker_api():
    docker_api = docker.APIClient(base_url='unix://var/run/docker.sock')
    return docker_api


@pytest.fixture()
def image_meta_data(docker_api, testvars):
    image_meta = docker_api.inspect_image(
        testvars['molecule_yml']['platforms'][0]['image'])
    return image_meta
