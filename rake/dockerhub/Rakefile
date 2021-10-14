# frozen_string_literal: true

require 'rake'

cmd_dockerhub_login = 'docker login'

cmd_dockerhub_push_custom = \
  'docker push ' \
  '%<target_user>s/%<target_repo>s:%<target_tag>s'

cmd_dockerhub_push_latest = \
  'docker push ' \
  '%<target_user>s/%<target_repo>s:latest'

cmd_dockerhub_push_version = \
  'docker push ' \
  '%<target_user>s/%<target_repo>s:%<version>s'

cmd_dockerhub_tag_custom = \
  'docker tag ' \
  '%<local_user>s/%<local_repo>s:latest ' \
  '%<target_user>s/%<target_repo>s:%<target_tag>s'

cmd_dockerhub_tag_latest = \
  'docker tag ' \
  '%<local_user>s/%<local_repo>s:latest ' \
  '%<target_user>s/%<target_repo>s:latest'

cmd_dockerhub_tag_version = \
  'docker tag ' \
  '%<local_user>s/%<local_repo>s:latest ' \
  '%<target_user>s/%<target_repo>s:%<version>s'

# rubocop:disable Metrics/BlockLength
namespace :dockerhub do
  desc 'Log in to hub.docker.com'
  task :login do
    @commands << cmd_dockerhub_login
  end

  @project['images'].each do |project_image|
    image = project_image.first
    namespace image.to_sym do
      next unless @project['images'][image].key?('target_user') &&
                  @project['images'][image].key?('target_repo')

      local_user = @project['local_user']
      local_repo = "#{@project['name']}-#{image}"
      target_user = @project['images'][image]['target_user']
      target_repo = @project['images'][image]['target_repo']
      version = @project['version']

      desc 'Push image to hub.docker.com'
      task push: [:"dockerhub:#{image}:push:version",
                  :"dockerhub:#{image}:push:latest"]

      namespace :push do
        desc 'Push latest image to hub.docker.com'
        task :latest do
          @commands << format(
            cmd_dockerhub_push_latest,
            target_user: target_user,
            target_repo: target_repo
          )
        end

        desc 'Push version image to hub.docker.com'
        task :version do
          @commands << format(
            cmd_dockerhub_push_version,
            target_user: target_user,
            target_repo: target_repo,
            version: version
          )
        end

        if @project['images'][image].key?('target_tag')
          target_tag = @project['images'][image]['target_tag']
          desc 'Push custom tagged image to hub.docker.com'
          task :custom do
            @commands << format(
              cmd_dockerhub_push_custom,
              target_user: target_user,
              target_repo: target_repo,
              target_tag: target_tag
            )
          end
        end
      end

      desc 'Tag image with latest tag for hub.docker.com'
      task tag: [:"dockerhub:#{image}:tag:version",
                 :"dockerhub:#{image}:tag:latest"]
      namespace :tag do
        desc 'Tag latest image for hub.docker.com'
        task :latest do
          @commands << format(
            cmd_dockerhub_tag_latest,
            local_user: local_user,
            local_repo: local_repo,
            target_user: target_user,
            target_repo: target_repo
          )
        end

        desc 'Tag image with version tag for hub.docker.com'
        task :version do
          @commands << format(
            cmd_dockerhub_tag_version,
            local_user: @project['local_user'],
            local_repo: local_repo,
            target_user: target_user,
            target_repo: target_repo,
            version: version
          )
        end

        if @project['images'][image].key?('target_tag')
          target_tag = @project['images'][image]['target_tag']
          desc 'Tag image with custom tag for hub.docker.com'
          task :custom do
            @commands << format(
              cmd_dockerhub_tag_custom,
              local_user: @project['local_user'],
              local_repo: local_repo,
              target_user: target_user,
              target_repo: target_repo,
              target_tag: target_tag
            )
          end
        end
      end
    end
  end
end
# rubocop:enable Metrics/BlockLength
