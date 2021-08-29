variable "ansible_playbook" {
  type    = string
  default = "{{ ansible_playbook }}"
}

source "vagrant" "takelage" {
  communicator       = "ssh"
  output_dir         = "images/vbox/takelbase/project"
  output_vagrantfile = "vagrantfile/vagrantfile.rb"
  provider           = "virtualbox"
  source_path        = "takelwerk/takelbase"
}

build {
  sources = ["source.vagrant.takelage"]

  provisioner "ansible" {
    ansible_env_vars = ["ANSIBLE_HOST_KEY_CHECKING=False", "ANSIBLE_SSH_ARGS='-v -o ControlMaster=auto -o ControlPersist=15m'"]
    extra_arguments  = ["-vvv"]
    groups           = ["all", "private", "users", "image", "vbox"]
    playbook_file    = "../ansible/${var.ansible_playbook}"
    user             = "vagrant"
  }

  provisioner "shell" {
    execute_command = "echo 'vagrant' | {{ .Vars }} sudo -S -E bash -eux '{{ .Path }}'"
    scripts         = ["templates/vbox/takelbase/project/bin/ssh.sh"]
  }
}
