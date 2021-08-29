variable "version" {
  type    = string
  default = ""
}

source "virtualbox-iso" "takelage" {
  boot_command            = [
    "<esc><wait>",
    "install <wait>",
    " preseed/url=http://{{ .HTTPIP }}:{{ .HTTPPort }}/preseed.cfg <wait>",
    "debian-installer=en_US.UTF-8 <wait>",
    "auto <wait>",
    "locale=en_US.UTF-8 <wait>",
    "kbd-chooser/method=de <wait>",
    "keyboard-configuration/xkb-keymap=de <wait>",
    "netcfg/get_hostname={{ .Name }} <wait>",
    "netcfg/get_domain=vagrantup.com <wait>",
    "fb=false <wait>",
    "debconf/frontend=noninteractive <wait>",
    "console-setup/ask_detect=false <wait>",
    "console-keymaps-at/keymap=de <wait>",
    "grub-installer/bootdev=/dev/sda <wait>",
    "<enter><wait>"
  ]
  boot_wait               = "5s"
  disk_size               = 81920
  guest_additions_path    = "VBoxGuestAdditions_{{ .Version }}.iso"
  guest_os_type           = "Debian_64"
  headless                = true
  http_directory          = "templates/vbox/takelbase/base/debian11/http"
  iso_checksum            = "sha256:ae6d563d2444665316901fe7091059ac34b8f67ba30f9159f7cef7d2fdc5bf8a"
  iso_urls                = [
    "iso/debian-11.0.0-amd64-netinst.iso",
    "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.0.0-amd64-netinst.iso"
  ]
  shutdown_command        = "echo 'vagrant'|sudo -S shutdown -P now"
  ssh_password            = "vagrant"
  ssh_port                = 22
  ssh_timeout             = "1800s"
  ssh_username            = "vagrant"
  vboxmanage              = [
    ["modifyvm", "{{ .Name }}", "--memory", "1024"],
    ["modifyvm", "{{ .Name }}", "--cpus", "1"]
  ]
  virtualbox_version_file = ".vbox_version"
  vm_name                 = "packer-debian-11-amd64"
}

build {
  sources = ["source.virtualbox-iso.takelage"]

  provisioner "shell" {
    execute_command = "echo 'vagrant' | {{ .Vars }} sudo -S -E bash -eux '{{ .Path }}'"
    scripts         = [
      "templates/vbox/takelbase/base/debian11/bin/ssh.sh",
      "templates/vbox/takelbase/base/debian11/bin/sudo.sh",
      "templates/vbox/takelbase/base/debian11/bin/guest.sh",
      "templates/vbox/takelbase/base/debian11/bin/apt.sh"]
  }

  post-processor "vagrant" {
    output = "images/vbox/takelbase/base/debian11/takelwerk-takelbase.box"
  }
}
