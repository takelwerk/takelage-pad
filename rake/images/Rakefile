# frozen_string_literal: true

require 'rake'

default_packer_template_dir = 'templates/takelage/docker'

cmd_images_docker_pull = 'docker pull ' \
  '%<base_user>s/%<base_repo>s:%<base_tag>s'

cmd_images_docker_pull_no_repo = 'docker pull ' \
  '%<base_user>s:%<base_tag>s'

cmd_images_docker_remove = 'docker image remove %<image>s'

cmd_images_molecule = \
  '%<env_command>s' \
  'TAKELAGE_UNIQUE=%<unique>s ' \
  'TAKELAGE_PROJECT_NAME=%<name>s ' \
  'TAKELAGE_PROJECT_IMG=%<image>s ' \
  'TAKELAGE_MOLECULE_VERIFIER_FILES=%<files>s ' \
  'TAKELAGE_MOLECULE_VERIFIER_PLAYS=%<plays>s ' \
  'bash -c ' \
  "'cd ansible && molecule %<job>s --scenario-name image'"

cmd_images_packer =
  'cd packer && ' \
  'packer build ' \
  "-var='ansible_playbook=%<playbook>s' " \
  "-var='image_name=%<image_name>s' " \
  "-var='base_repo=%<base_repo>s' " \
  "-var='base_user=%<base_user>s' " \
  "-var='base_tag=%<base_tag>s' " \
  "-var='local_user=%<local_user>s' " \
  "-var='target_repo=%<target_repo>s' " \
  "-var='packer_template_dir='%<packer_template_dir>s'' " \
  '%<var_privileged>s' \
  '%<var_packer_command>s' \
  '%<var_command>s' \
  '%<var_entrypoint>s' \
  '%<var_workdir>s' \
  '%<packer_template_dir>s'

jobs = \
  %i[converge
     destroy
     lint
     login
     test
     verify]

# rubocop:disable Metrics/BlockLength
namespace :images do
  name = @project['name']
  images = @project['images']
  images.each do |project_image|
    image = project_image.first
    keep_interim_images = images[image]['keep_interim_images'].nil? ? true : images[image]['keep_interim_images']
    namespace image.to_sym do |env|
      subtasks(env.scope.path) do
        desc 'Update docker base image'
        task :update do
          @commands << if images[image].key?('base_repo')
                         format(
                           cmd_images_docker_pull,
                           base_user: images[image]['base_user'],
                           base_repo: images[image]['base_repo'],
                           base_tag: images[image]['base_tag']
                         )
                       else
                         format(
                           cmd_images_docker_pull_no_repo,
                           base_user: images[image]['base_user'],
                           base_tag: images[image]['base_tag']
                         )
                       end
        end

        layers = images[image]['layers']
        if layers.count == 1
          desc "Build image #{image}"
          task build: "build:layer:01-#{layers.first}"
        else
          # more than one layer
          namespace :build do
            namespace :to do
              layers[0..].each_with_index do |layer, index|
                number = index.next.to_s.rjust(2, '0')
                dependencies = []
                remove_last_layer = nil
                layers[0..-2].each_with_index do |sublayer, subindex|
                  next if index < subindex

                  subnumber = subindex.next.to_s.rjust(2, '0')
                  dependencies << "images:#{image}:build:layer:#{subnumber}-#{sublayer}".to_sym
                  dependencies << remove_last_layer unless remove_last_layer.nil? || keep_interim_images
                  remove_last_layer = "images:#{image}:remove:layer:#{subnumber}-#{sublayer}".to_sym
                end
                desc "Build layers up to layer #{layer} of image #{image}"
                task "#{number}-#{layer}".to_sym => dependencies
              end
            end

            namespace :from do
              layers[0..].each_with_index do |layer, index|
                number = index.next.to_s.rjust(2, '0')
                dependencies = []
                remove_last_layer = nil
                layers[0..].each_with_index do |sublayer, subindex|
                  next if index >= subindex

                  subnumber = subindex.next.to_s.rjust(2, '0')
                  dependencies << "images:#{image}:build:layer:#{subnumber}-#{sublayer}".to_sym
                  dependencies << remove_last_layer unless remove_last_layer.nil? || keep_interim_images
                  remove_last_layer = "images:#{image}:remove:layer:#{subnumber}-#{sublayer}".to_sym
                end
                desc "Build layers from to layer #{layer} of image #{image}"
                task "#{number}-#{layer}".to_sym => dependencies
              end
            end
          end
        end

        namespace :build do
          namespace :layer do
            parent_layer = ''
            layers.each_with_index do |layer, index|
              parent_number = index.to_s.rjust(2, '0')
              number = index.next.to_s.rjust(2, '0')
              target_repo = "#{@project['name']}-#{image}-#{number}-#{layer}"
              # first image
              if index.zero?
                base_repo = images[image]['base_repo']
                base_user = images[image]['base_user']
                base_tag = images[image]['base_tag']
              else
                base_repo = "#{@project['name']}-#{image}-#{parent_number}-#{parent_layer}"
                base_user = @project['local_user']
                base_tag = 'latest'
              end
              # last
              target_repo = "#{@project['name']}-#{image}" if index.next == layers.count

              packer_template_dir = images[image]['packer_template_dir'] || default_packer_template_dir

              # rubocop:disable Style/IfUnlessModifier
              var_privileged = ''
              if images[image].key?('privileged')
                var_privileged = "-var='privileged=#{images[image]['privileged']}' "
              end

              var_command = ''
              if images[image].key?('command')
                var_command = "-var='command=#{images[image]['command']}' "
              end

              var_entrypoint = ''
              if images[image].key?('entrypoint')
                var_entrypoint = "-var='entrypoint=#{images[image]['entrypoint']}' "
              end

              var_workdir = ''
              if images[image].key?('workdir')
                var_workdir = "-var='workdir=#{images[image]['workdir']}' "
              end

              var_packer_command = ''
              if images[image].key?('packer_command')
                var_packer_command = "-var='packer_command=#{images[image]['packer_command']}' "
              end
              # rubocop:enable Style/IfUnlessModifier

              parent_layer = layer

              # desc "Build layer #{layer} from base layer #{parent_layer} of image #{image}"
              task "#{number}-#{layer}".to_sym do
                @commands << format(
                  cmd_images_packer,
                  image_name: image,
                  playbook: "playbook-#{layer}.yml",
                  base_repo: base_repo,
                  base_user: base_user,
                  base_tag: base_tag,
                  local_user: @project['local_user'],
                  packer_template_dir: packer_template_dir,
                  var_privileged: var_privileged,
                  var_packer_command: var_packer_command,
                  var_command: var_command,
                  var_entrypoint: var_entrypoint,
                  var_workdir: var_workdir,
                  target_repo: target_repo
                )
              end
            end
          end
        end

        namespace :remove do
          namespace :layer do
            layers.each_with_index do |layer, index|
              number = index.next.to_s.rjust(2, '0')
              user = @project['local_user']
              repo = "#{@project['name']}-#{image}-#{number}-#{layer}"
              tag = 'latest'
              # desc "Remove layer #{layer} of image #{image}"
              task "#{number}-#{layer}".to_sym do
                @commands << format(
                  cmd_images_docker_remove,
                  image: "#{user}/#{repo}:#{tag}"
                )
              end
            end
          end
        end

        if File.exist?("#{File.dirname(__FILE__)}/../../ansible/molecule/image")
          namespace :molecule do
            env_command = ''
            env_command = "TAKELAGE_PROJECT_COMMAND='#{images[image]['command']}' " if images[image].key?('command')

            begin
              unique = ENV['HOSTNAME'][-11..]
            rescue StandardError
              unique = 'nonunique'
            end

            jobs.each do |job|
              desc "#{job.capitalize} image #{image}"
              task job.to_sym do
                @commands << format(
                  cmd_images_molecule,
                  env_command: env_command,
                  files: molecule_verifier_files(layers),
                  image: image,
                  job: job,
                  name: name,
                  plays: molecule_verifier_plays(layers),
                  unique: unique
                )
              end
            end
          end
        end
      end
    end
  end
end
# rubocop:enable Metrics/BlockLength

private

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

def molecule_verifier_plays(layers)
  verifier_plays = []
  layers.each do |layer|
    verifier_plays << "../../playbook-#{layer}.yml"
  end
  "'#{verifier_plays.join(':')}'"
end
