variable "ansible_connection" {
  type = string
  default = "docker"
}

variable "image_name" {
  type = string
}

variable "ansible_playbook" {
  type = string
}

variable "base_repo" {
  type = string
}

variable "base_tag" {
  type = string
  default = "latest"
}

variable "base_user" {
  type = string
}

variable "local_user" {
  type = string
}

variable "mutagen" {
  type = string
  default = "invalid"
}

variable "target_repo" {
  type = string
}

variable "target_tag" {
  type = string
  default = "latest"
}

variable "packer_template_dir" {
  type = string
}

variable "privileged" {
  type = string
  default = "false"
}

variable "packer_command" {
  type = string
  default = "/usr/bin/tail -f /dev/null"
}

variable "command" {
  type = string
  default = "/usr/bin/tail -f /dev/null"
}

locals {
  ansible_host = "${var.target_repo}"
  privileged_list = "${var.privileged}" == "true" ? ["--privileged"] : []
  run_command_arguments = [
    "--detach",
    "--interactive",
    "--tty",
    "--name",
    "${var.target_repo}",
    "{{ .Image }}"
  ]
  run_command_split = split(" ", "${var.packer_command}")
  run_command = concat(concat(
    "${local.privileged_list}", "${local.run_command_arguments}"),
    "${local.run_command_split}"
  )
}
