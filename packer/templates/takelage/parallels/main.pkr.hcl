source "vagrant" "takelage" {
  communicator       = "ssh"
  output_dir         = "images/pvm/${var.target_user}-${var.target_repo}"
  output_vagrantfile = "vagrantfile/vagrantfile.rb"
  provider           = "parallels"
  source_path        = "${var.base_user}/${var.base_repo}"
}

build {
  sources = ["source.vagrant.takelage"]

  provisioner "ansible" {
    ansible_env_vars = ["ANSIBLE_HOST_KEY_CHECKING=False", "ANSIBLE_SSH_ARGS='-v -o ControlMaster=auto -o ControlPersist=15m ${var.ansible_ssh_legacy}'"]
    extra_arguments  = ["-vvv"]
    groups           = ["all", "private", "users", "image", "pvm"]
    playbook_file    = "../ansible/${var.ansible_playbook}"
    user             = "vagrant"
  }

  provisioner "shell" {
    execute_command = "echo 'vagrant' | {{ .Vars }} sudo -S -E bash -eux '{{ .Path }}'"
    scripts         = ["${var.packer_template_dir}/bin/ssh.sh"]
  }
}
