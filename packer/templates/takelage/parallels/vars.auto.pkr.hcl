variable "base_user" {
  type = string
}

variable "base_repo" {
  type = string
}

variable "target_user" {
  type = string
}

variable "target_repo" {
  type = string
}

variable "target_version" {
  type = string
}

variable "packer_template_dir" {
  type = string
}

variable "ansible_playbook" {
  type    = string
  default = "playbook-site.yml"
}

variable "ansible_ssh_legacy" {
  type    = string
  default = ""
}
