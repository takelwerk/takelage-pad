# frozen_string_literal: true

require 'rake'

default_packer_template_dir = 'templates/takelage/virtualbox'

cmd_vboxes_vbox_update = 'vagrant box update ' \
  '--box %<base_user>s/%<base_repo>s ' \
  '--provider virtualbox'

cmd_vboxes_packer = 'cd packer && ' \
  'mkdir -p images/vbox && ' \
  'packer build ' \
  "-var='base_user=%<base_user>s' " \
  "-var='base_repo=%<base_repo>s' " \
  "-var='target_user=%<target_user>s' " \
  "-var='target_repo=%<target_repo>s' " \
  "-var='target_version=%<target_version>s' " \
  "-var='packer_template_dir=%<packer_template_dir>s' " \
  '%<packer_template_dir>s'

cmd_vboxes_packer_withlegacyssh = 'cd packer && ' \
  'mkdir -p images/vbox && ' \
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
namespace :vboxes do
  vboxes = @project['vboxes']
  vboxes.each do |project_vbox|
    vbox = project_vbox.first
    namespace vbox.to_sym do |env|
      subtasks(env.scope.path) do
        if @project['vboxes'][vbox].key?('base_user') &&
           @project['vboxes'][vbox].key?('base_repo')
          desc 'Update docker base image'
          task :update do
            @commands << format(
              cmd_vboxes_vbox_update,
              base_repo: vboxes[vbox]['base_repo'],
              base_user: vboxes[vbox]['base_user']
            )
          end
        end

        base_user = ''
        base_user = @project['vboxes'][vbox]['base_user'] if @project['vboxes'][vbox].key?('base_user')
        base_repo = ''
        base_repo = @project['vboxes'][vbox]['base_repo'] if @project['vboxes'][vbox].key?('base_repo')
        target_user = @project['vboxes'][vbox]['target_user']
        target_repo = @project['vboxes'][vbox]['target_repo']
        target_version = @project['version']
        ansible_playbook = 'playbook-site.yml'
        if @project['vboxes'][vbox].key?('ansible_playbook')
          ansible_playbook = @project['vboxes'][vbox]['ansible_playbook']
        end
        ansible_ssh_legacy = '-oHostKeyAlgorithms=+ssh-rsa -oPubkeyAcceptedAlgorithms=+ssh-rsa'
        packer_template_dir = vboxes[vbox]['packer_template_dir'] || default_packer_template_dir

        desc 'Build virtualbox'
        task :build do
          @commands << format(
            cmd_vboxes_packer,
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
              cmd_vboxes_packer_withlegacyssh,
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
