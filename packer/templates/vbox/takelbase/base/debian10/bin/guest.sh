#!/bin/bash -eux

VBOX_VERSION=$(cat /home/vagrant/.vbox_version)

mkdir -p /media/guestadditions
mount -o loop /home/vagrant/VBoxGuestAdditions_${VBOX_VERSION}.iso /media/guestadditions
/media/guestadditions/VBoxLinuxAdditions.run || true
umount /media/guestadditions
rm /home/vagrant/VBoxGuestAdditions_${VBOX_VERSION}.iso
rm -fr /media/guestadditions
