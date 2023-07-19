# frozen_string_literal: true

require 'rake'

cmd_dockerhub_login = 'pass show dev/takelwerk/dockerhub/token | ' \
  'docker login --password-stdin ' \
  '--username $(pass show dev/takelwerk/dockerhub/user)'

cmd_dockerhub_manifest_create_latest = \
  'docker manifest create --amend ' \
  '%<target_user>s/%<target_repo>s:latest ' \
  '%<target_user>s/%<target_repo>s:latest-amd64 ' \
  '%<target_user>s/%<target_repo>s:latest-arm64'

cmd_dockerhub_manifest_create_version = \
  'docker manifest create --amend ' \
  '%<target_user>s/%<target_repo>s:%<version>s ' \
  '%<target_user>s/%<target_repo>s:%<version>s-amd64 ' \
  '%<target_user>s/%<target_repo>s:%<version>s-arm64'

cmd_dockerhub_manifest_push_latest = \
  'docker manifest push --purge ' \
  '%<target_user>s/%<target_repo>s:latest'

cmd_dockerhub_manifest_push_version = \
  'docker manifest push --purge ' \
  '%<target_user>s/%<target_repo>s:%<version>s'

cmd_dockerhub_pull_latest = \
  'docker pull ' \
  '%<target_user>s/%<target_repo>s:latest-%<target_arch>s'

cmd_dockerhub_pull_version = \
  'docker pull ' \
  '%<target_user>s/%<target_repo>s:%<version>s-%<target_arch>s'

cmd_dockerhub_push_latest = \
  'docker push ' \
  '%<target_user>s/%<target_repo>s:latest-%<target_arch>s'

cmd_dockerhub_push_version = \
  'docker push ' \
  '%<target_user>s/%<target_repo>s:%<version>s-%<target_arch>s'

cmd_dockerhub_push_custom = \
  'docker push ' \
  '%<target_user>s/%<target_repo>s:%<target_tag>s-%<target_arch>s'

cmd_dockerhub_tag_latest = \
  'docker tag ' \
  '%<local_user>s/%<local_repo>s:latest ' \
  '%<target_user>s/%<target_repo>s:latest-%<target_arch>s'

cmd_dockerhub_tag_version = \
  'docker tag ' \
  '%<local_user>s/%<local_repo>s:latest ' \
  '%<target_user>s/%<target_repo>s:%<version>s-%<target_arch>s'

cmd_dockerhub_tag_custom = \
  'docker tag ' \
  '%<local_user>s/%<local_repo>s:latest ' \
  '%<target_user>s/%<target_repo>s:%<target_tag>s-%<target_arch>s'

# rubocop:disable Metrics/BlockLength
namespace :dockerhub do
  desc 'Log in to hub.docker.com'
  task :login do
    @commands << cmd_dockerhub_login
  end

  @project['images'].each do |project_image|
    image = project_image.first
    namespace image.to_sym do |env|
      subtasks(env.scope.path) do
        next unless @project['images'][image].key?('target_user') &&
                    @project['images'][image].key?('target_repo')

        local_user = @project['local_user']
        local_repo = "#{@project['name']}-#{image}"
        target_user = @project['images'][image]['target_user']
        target_repo = @project['images'][image]['target_repo']
        version = @project['version']

        namespace :manifest do
          namespace :create do
            desc 'Create latest docker manifest'
            task :latest do
              @commands << format(
                cmd_dockerhub_manifest_create_latest,
                target_user: target_user,
                target_repo: target_repo
              )
            end

            desc 'Create version docker manifest'
            task :version do
              @commands << format(
                cmd_dockerhub_manifest_create_version,
                target_user: target_user,
                target_repo: target_repo,
                version: version
              )
            end
          end

          namespace :push do
            desc 'Push latest docker manifest'
            task :latest do
              @commands << format(
                cmd_dockerhub_manifest_push_latest,
                target_user: target_user,
                target_repo: target_repo
              )
            end

            desc 'Push version docker manifest'
            task :version do
              @commands << format(
                cmd_dockerhub_manifest_push_version,
                target_user: target_user,
                target_repo: target_repo,
                version: version
              )
            end
          end
        end

        namespace :pull do
          namespace :latest do
            desc 'Pull latest amd64 image from hub.docker.com'
            task :amd64 do
              @commands << format(
                cmd_dockerhub_pull_latest,
                target_user: target_user,
                target_repo: target_repo,
                target_arch: 'amd64'
              )
            end

            desc 'Pull latest amd64 image from hub.docker.com'
            task :arm64 do
              @commands << format(
                cmd_dockerhub_pull_latest,
                target_user: target_user,
                target_repo: target_repo,
                target_arch: 'arm64'
              )
            end
          end

          namespace :version do
            desc 'Pull version amd64 image from hub.docker.com'
            task :amd64 do
              @commands << format(
                cmd_dockerhub_pull_version,
                target_user: target_user,
                target_repo: target_repo,
                version: version,
                target_arch: 'amd64'
              )
            end

            desc 'Push version amd64 image from hub.docker.com'
            task :arm64 do
              @commands << format(
                cmd_dockerhub_pull_version,
                target_user: target_user,
                target_repo: target_repo,
                version: version,
                target_arch: 'arm64'
              )
            end
          end
        end

        namespace :push do
          namespace :latest do
            desc 'Push latest amd64 image to hub.docker.com'
            task :amd64 do
              @commands << format(
                cmd_dockerhub_push_latest,
                target_user: target_user,
                target_repo: target_repo,
                target_arch: 'amd64'
              )
            end

            desc 'Push latest amd64 image to hub.docker.com'
            task :arm64 do
              @commands << format(
                cmd_dockerhub_push_latest,
                target_user: target_user,
                target_repo: target_repo,
                target_arch: 'arm64'
              )
            end
          end

          namespace :version do
            desc 'Push version amd64 image to hub.docker.com'
            task :amd64 do
              @commands << format(
                cmd_dockerhub_push_version,
                target_user: target_user,
                target_repo: target_repo,
                version: version,
                target_arch: 'amd64'
              )
            end

            desc 'Push version amd64 image to hub.docker.com'
            task :arm64 do
              @commands << format(
                cmd_dockerhub_push_version,
                target_user: target_user,
                target_repo: target_repo,
                version: version,
                target_arch: 'arm64'
              )
            end
          end

          namespace :custom do
            if @project['images'][image].key?('target_tag')
              target_tag = @project['images'][image]['target_tag']
              desc 'Push custom tagged amd64 image to hub.docker.com'
              task :amd64 do
                @commands << format(
                  cmd_dockerhub_push_custom,
                  target_user: target_user,
                  target_repo: target_repo,
                  target_tag: target_tag,
                  target_arch: 'amd64'
                )
              end

              desc 'Push custom tagged amd64 image to hub.docker.com'
              task :arm64 do
                @commands << format(
                  cmd_dockerhub_push_custom,
                  target_user: target_user,
                  target_repo: target_repo,
                  target_tag: target_tag,
                  target_arch: 'arm64'
                )
              end
            end
          end
        end

        namespace :tag do
          namespace :latest do
            desc 'Tag latest amd64 image for hub.docker.com'
            task :amd64 do
              @commands << format(
                cmd_dockerhub_tag_latest,
                local_user: local_user,
                local_repo: local_repo,
                target_user: target_user,
                target_repo: target_repo,
                target_arch: 'amd64'
              )
            end

            desc 'Tag latest arm64 image for hub.docker.com'
            task :arm64 do
              @commands << format(
                cmd_dockerhub_tag_latest,
                local_user: local_user,
                local_repo: local_repo,
                target_user: target_user,
                target_repo: target_repo,
                target_arch: 'arm64'
              )
            end
          end

          namespace :version do
            desc 'Tag version amd64 image for hub.docker.com'
            task :amd64 do
              @commands << format(
                cmd_dockerhub_tag_version,
                local_user: local_user,
                local_repo: local_repo,
                target_user: target_user,
                target_repo: target_repo,
                version: version,
                target_arch: 'amd64'
              )
            end

            desc 'Tag version arm64 image for hub.docker.com'
            task :arm64 do
              @commands << format(
                cmd_dockerhub_tag_version,
                local_user: local_user,
                local_repo: local_repo,
                target_user: target_user,
                target_repo: target_repo,
                version: version,
                target_arch: 'arm64'
              )
            end
          end

          if @project['images'][image].key?('target_tag')
            target_tag = @project['images'][image]['target_tag']
            namespace :custom do
              desc 'Tag custom amd64 image for hub.docker.com'
              task :amd64 do
                @commands << format(
                  cmd_dockerhub_tag_custom,
                  local_user: local_user,
                  local_repo: local_repo,
                  target_user: target_user,
                  target_repo: target_repo,
                  target_tag: target_tag,
                  target_arch: 'amd64'
                )
              end

              desc 'Tag custom arm64 image for hub.docker.com'
              task :arm64 do
                @commands << format(
                  cmd_dockerhub_tag_custom,
                  local_user: local_user,
                  local_repo: local_repo,
                  target_user: target_user,
                  target_repo: target_repo,
                  target_tag: target_tag,
                  target_arch: 'arm64'
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
