# frozen_string_literal: true

require 'rake'

cmd_ansible_molecule_lint =
  'set -e && yamllint . && ansible-lint . && flake8'

cmd_ansible_molecule_project_lint =
  "cd ansible && bash -c '" \
  "#{cmd_ansible_molecule_lint}'"

cmd_ansible_molecule_project =
  "cd ansible && bash -c '" \
  '%<env_command>s' \
  'TAKELAGE_UNIQUE=%<unique>s ' \
  'TAKELAGE_PROJECT_NAME=%<projectname>s ' \
  'TAKELAGE_PROJECT_BASE_IMG=%<image>s ' \
  'TAKELAGE_MOLECULE_VERIFIER_FILES=%<files>s ' \
  'TAKELAGE_MOLECULE_CONVERGE_PLAYBOOK=%<playbook>s ' \
  "molecule %<job>s --scenario-name default'"

cmd_ansible_molecule_role =
  "cd %<role_path>s && bash -c '" \
  "molecule %<job>s'"

cmd_ansible_molecule_role_lint =
  "cd %<role_path>s && bash -c '" \
  "#{cmd_ansible_molecule_lint}'"

cmd_ansible_roles_test_all =
  'for dir in ' \
  '`find ansible/roles -maxdepth 2 -name molecule | sort`; ' \
  'do ' \
  'cd `dirname $dir`; ' \
  'molecule test --all; ' \
  'cd ../../../; ' \
  'done'

cmd_ansible_roles_test_each =
  'for dir in ' \
  '`find ansible/roles -maxdepth 2 -name molecule | sort`; ' \
  'do ' \
  'cd `dirname $dir`; ' \
  'molecule test --all || exit; ' \
  'cd ../../../; ' \
  'done'

jobs_project = \
  %i[converge
     destroy
     list
     login
     test
     verify]

jobs_roles = \
  %i[converge
     destroy
     login
     test
     verify]

# rubocop:disable Metrics/BlockLength
namespace :ansible do
  namespace :molecule do |env|
    subtasks(env.scope.path) do
      image = @project['images']['project']
      env_command = ''
      if image.key?('command')
        img_cmd = image['command'].join(' ')
        env_command = "TAKELAGE_PROJECT_COMMAND=\"#{img_cmd}\" "
      end

      begin
        unique = ENV['HOSTNAME'][-11..]
      rescue StandardError
        unique = 'nonunique'
      end

      jobs_project.each do |job|
        desc "Run molecule #{job}"
        task job do
          @commands << format(
            cmd_ansible_molecule_project,
            env_command: env_command,
            job: job,
            playbook: 'playbook-site.yml',
            files: molecule_verifier_files(['site']),
            projectname: @project['name'],
            image:
              "#{@project['images']['project']['base_user']}/" \
                "#{@project['images']['project']['base_repo']}:" \
                "#{@project['images']['project']['base_tag']}",
            unique: unique
          )
        end
      end
      desc 'Run molecule lint'
      task 'lint' do
        @commands << cmd_ansible_molecule_project_lint
      end
    end
  end

  namespace :roles do |env|
    desc 'Run molecule tests for all roles skipping errors'
    task :all do
      @commands << cmd_ansible_roles_test_all
    end

    desc 'Run molecule tests for each role failing in case of errors'
    task :each do
      @commands << cmd_ansible_roles_test_each
    end

    subtasks(env.scope.path) do
      Dir.glob('ansible/roles/*/molecule').each do |role_path|
        role = role_path.match(%r{roles/(?<role_name>.*)/molecule})
        namespace role[:role_name] do
          jobs_roles.each do |job|
            desc "Run molecule #{job} for #{role[:role_name]}"
            task job do
              @commands << format(
                cmd_ansible_molecule_role,
                job: job,
                role_path: role_path.split('/molecule')[0]
              )
            end
          end
          desc "Run molecule lint for #{role[:role_name]}"
          task 'lint' do
            @commands << format(
              cmd_ansible_molecule_role_lint,
              role_path: role_path.split('/molecule')[0]
            )
          end
        end
      end
    end
  end
end
# rubocop:enable Metrics/BlockLength

# rubocop:disable Metrics/MethodLength
def molecule_verifier_files(layers)
  verifier_files = []
  layers.each do |layer|
    playbook = YAML.safe_load(File.read("ansible/playbook-#{layer}.yml"))
    playbook[0]['roles'].each do |role|
      rolename = role
      rolename = role['role'] if role.is_a?(Hash) && role.key?('role')
      verifier_files << "\"../../../roles/#{rolename}/molecule/default/system/test_*.py\""
      verifier_files << "\"../../../roles/#{rolename}/molecule/default/tests/test_*.py\""
    end
  end
  "'[#{verifier_files.join(',')}]'"
end

# rubocop:enable Metrics/MethodLength
