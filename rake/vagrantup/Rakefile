# frozen_string_literal: true

require 'rake'

cmd_vagrantup_login = 'vagrant cloud auth login'

cmd_vagrantup_push = 'cd packer && ' \
    'vagrant cloud publish ' \
    '--force ' \
    '--release ' \
    '%<target_user>s/%<target_repo>s ' \
    '%<target_version>s ' \
    '%<provider>s ' \
    'images/%<image_name>s/%<target_user>s-%<target_repo>s/package.box'

# rubocop:disable Metrics/BlockLength
namespace :vagrantup do
  desc 'Log in to app.vagrantup.com'
  task :login do
    @commands << cmd_vagrantup_login
  end

  if @project.key?('pvms')
    namespace :parallels do
      @project['pvms'].each do |project_pvm|
        pvm = project_pvm.first
        namespace pvm.to_sym do
          next unless @project['pvms'][pvm].key?('target_user') &&
                      @project['pvms'][pvm].key?('target_repo')

          target_user = @project['pvms'][pvm]['target_user']
          target_repo = @project['pvms'][pvm]['target_repo']
          target_version = @project['version']

          desc 'Push pvm to app.vagrantup.com'
          task :push do
            @commands << format(
              cmd_vagrantup_push,
              provider: 'parallels',
              image_name: 'pvm',
              target_user: target_user,
              target_repo: target_repo,
              target_version: target_version
            )
          end
        end
      end
    end
  end

  if @project.key?('vboxes')
    namespace :virtualbox do
      @project['vboxes'].each do |project_vbox|
        vbox = project_vbox.first
        namespace vbox.to_sym do
          next unless @project['vboxes'][vbox].key?('target_user') &&
                      @project['vboxes'][vbox].key?('target_repo')

          target_user = @project['vboxes'][vbox]['target_user']
          target_repo = @project['vboxes'][vbox]['target_repo']
          target_version = @project['version']

          desc 'Push vbox to app.vagrantup.com'
          task :push do
            @commands << format(
              cmd_vagrantup_push,
              provider: 'virtualbox',
              image_name: 'vbox',
              target_user: target_user,
              target_repo: target_repo,
              target_version: target_version
            )
          end
        end
      end
    end
  end
end
# rubocop:enable Metrics/BlockLength
