# frozen_string_literal: true

@cmd_ansible_project = "cd ansible && bash -c '" \
        'TAKELAGE_PROJECT_ENV=%<project_environment>s ' \
        'TAKELAGE_PROJECT_BASE_IMAGE=%<image>s ' \
        'TAKELAGE_MOLECULE_CONVERGE_PLAYBOOK=%<converge_playbook>s ' \
        "molecule %<command>s --scenario-name default'"

@list_ansible_project = %i[converge destroy login test verify]
