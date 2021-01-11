# frozen_string_literal: true

require 'rake'

cmd_git_tag = 'git rev-parse ' \
    "#{@project['version']} " \
    '>/dev/null 2>&1 || ' \
    '(git tag -s -m ' \
    "'#{@project['version']}' " \
    "#{@project['version']} && " \
    'git push --tags)'

cmd_git_warn = 'git rev-parse ' \
    "#{@project['version']} " \
    '>/dev/null 2>&1 && ' \
    'echo -e "\n\n\e[31m' \
    "git tag #{@project['version']} already exists! " \
    '\e[0m\n"; ' \
    'true'

namespace :git do
  desc 'Create and push git tag'
  task :tag do
    @commands << cmd_git_tag
  end

  desc 'Warn if git tag already exists'
  task :warn do
    @commands << cmd_git_warn
  end
end
