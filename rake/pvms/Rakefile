# frozen_string_literal: true

require 'rake'

default_packer_template_dir = 'templates/takelage/parallels'

cmd_pvms_pvm_update = 'vagrant box update ' \
  '--box %<base_user>s/%<base_repo>s ' \
  '--provider parallels'

cmd_pvms_packer = 'cd packer && ' \
  'mkdir -p images/pvm && ' \
  'packer build ' \
  "-var='base_user=%<base_user>s' " \
  "-var='base_repo=%<base_repo>s' " \
  "-var='target_user=%<target_user>s' " \
  "-var='target_repo=%<target_repo>s' " \
  "-var='target_version=%<target_version>s' " \
  "-var='packer_template_dir=%<packer_template_dir>s' " \
  '%<packer_template_dir>s'

cmd_pvms_packer_withlegacyssh = 'cd packer && ' \
  'mkdir -p images/pvm && ' \
  'packer build ' \
  "-var='base_user=%<base_user>s' " \
  "-var='base_repo=%<base_repo>s' " \
  "-var='target_user=%<target_user>s' " \
  "-var='target_repo=%<target_repo>s' " \
  "-var='target_version=%<target_version>s' " \
  "-var='packer_template_dir=%<packer_template_dir>s' " \
  "-var='ansible_ssh_legacy=%<ansible_ssh_legacy>s' " \
  '%<packer_template_dir>s'

# rubocop:disable Metrics/BlockLength
namespace :pvms do
  pvms = @project['pvms']
  pvms.each do |project_pvm|
    pvm = project_pvm.first
    namespace pvm.to_sym do |env|
      subtasks(env.scope.path) do
        if @project['pvms'][pvm].key?('base_user') &&
           @project['pvms'][pvm].key?('base_repo')
          desc 'Update docker base image'
          task :update do
            @commands << format(
              cmd_pvms_pvm_update,
              base_repo: pvms[pvm]['base_repo'],
              base_user: pvms[pvm]['base_user']
            )
          end
        end

        base_user = ''
        base_user = @project['pvms'][pvm]['base_user'] if @project['pvms'][pvm].key?('base_user')
        base_repo = ''
        base_repo = @project['pvms'][pvm]['base_repo'] if @project['pvms'][pvm].key?('base_repo')
        target_user = @project['pvms'][pvm]['target_user']
        target_repo = @project['pvms'][pvm]['target_repo']
        target_version = @project['version']
        ansible_playbook = 'playbook-site.yml'
        ansible_playbook = @project['pvms'][pvm]['ansible_playbook'] if @project['pvms'][pvm].key?('ansible_playbook')
        ansible_ssh_legacy = '-oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa'
        packer_template_dir = pvms[pvm]['packer_template_dir'] || default_packer_template_dir

        desc 'Build parallels vm'
        task :build do
          @commands << format(
            cmd_pvms_packer,
            base_user: base_user,
            base_repo: base_repo,
            target_user: target_user,
            target_repo: target_repo,
            target_version: target_version,
            ansible_playbook: ansible_playbook,
            packer_template_dir: packer_template_dir
          )
        end

        namespace :build do
          desc 'Build virtualbox with ansible legacy ssh'
          task :withlegacyssh do
            @commands << format(
              cmd_pvms_packer_withlegacyssh,
              base_user: base_user,
              base_repo: base_repo,
              target_user: target_user,
              target_repo: target_repo,
              target_version: target_version,
              ansible_playbook: ansible_playbook,
              ansible_ssh_legacy: ansible_ssh_legacy,
              packer_template_dir: packer_template_dir
            )
          end
        end
      end
    end
  end
end
# rubocop:enable Metrics/BlockLength
