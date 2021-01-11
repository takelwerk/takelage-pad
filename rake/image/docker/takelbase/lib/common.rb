# frozen_string_literal: true

require 'rake'

@cmd_image_base = {
  debian10: 'docker pull debian:buster-slim && ' \
        'mkdir -p packer/images/debian/buster && ' \
        'cd packer && packer build ' \
        "--var 'base_repo=debian' " \
        "--var 'base_tag=buster-slim' " \
        "--var 'target_user=#{@project['local_user']}' " \
        "--var 'target_repo=#{@project['dockerhub_base_tag']}' " \
        "--var 'target_tag=latest' " \
        'templates/docker/takelbase/base/debian10/packer.json'
}

@cmd_image_project = {
  from_base: 'cd packer && packer build ' \
             "--var 'ansible_environment=%<project_environment>s' " \
             "--var 'ansible_playbook=playbook-project-base.yml' " \
             "--var 'base_repo=#{@project['dockerhub_base_repo']}' " \
             "--var 'base_user=#{@project['dockerhub_base_user']}' " \
             "--var 'base_tag=latest' " \
             "--var 'local_user=#{@project['local_user']}' " \
             "--var 'target_repo=#{@project['name']}' " \
             "--var 'target_tag=%<project_environment>s' " \
             'templates/docker/takelbase/project/build_from_base.json',
  from_prod: 'cd packer && ' \
             'packer build ' \
             "--var 'ansible_environment=%<project_environment>s' " \
             "--var 'ansible_playbook=playbook-project-from-prod.yml' " \
             "--var 'base_repo=#{@project['name']}' " \
             "--var 'base_user=#{@project['local_user']}' " \
             "--var 'base_tag=prod' " \
             "--var 'hatch=${TAKELAGE_PROJECT_BASE_DIR}/" \
             "ansible/molecule/support/hatch/stage:/takelage/hatch:ro' " \
             "--var 'local_user=#{@project['local_user']}' " \
             "--var 'target_repo=#{@project['name']}' " \
             "--var 'target_tag=%<project_environment>s' " \
             'templates/docker/takelbase/project/build_from_prod.json',
  test: 'TAKELAGE_PROJECT_ENV=%<project_environment>s bash -c ' \
        "'cd ansible && molecule test --scenario-name image'",
  login: 'TAKELAGE_PROJECT_ENV=%<project_environment>s bash -c ' \
        "'cd ansible && molecule login --scenario-name image'",
  create: 'TAKELAGE_PROJECT_ENV=%<project_environment>s bash -c ' \
        "'cd ansible && molecule create --scenario-name image'",
  verify: 'TAKELAGE_PROJECT_ENV=%<project_environment>s bash -c ' \
        "'cd ansible && molecule verify --scenario-name image'",
  destroy: 'TAKELAGE_PROJECT_ENV=%<project_environment>s bash -c ' \
        "'cd ansible && molecule destroy --scenario-name image'"

}
