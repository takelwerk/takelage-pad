# frozen_string_literal: true

require 'rake'

@cmd_local_molecule_command = \
  'cd ansible && ' \
  'TAKELAGE_PROJECT_ENV=%<project_environment>s ' \
  'molecule %<molecule_command>s --scenario-name local'

@cmd_local_list = %i[converge destroy login features verify]
