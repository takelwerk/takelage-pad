# frozen_string_literal: true

@cmd_ansible_docker_takelbase_project = "cd ansible && bash -c '" \
        'TAKELAGE_PROJECT_ENV=%<project_environment>s ' \
        'TAKELAGE_PROJECT_BASE_IMAGE=%<image>s ' \
        "TAKELAGE_PROJECT_NAME=#{@project['name']} " \
        'TAKELAGE_MOLECULE_CONVERGE_PLAYBOOK=%<converge_playbook>s ' \
        "molecule %<command>s --scenario-name default'"

@list_ansible_docker_takelbase_project = %i[converge
                                            destroy
                                            lint
                                            list
                                            login
                                            test
                                            prepare
                                            verify
                                            side-effect]
