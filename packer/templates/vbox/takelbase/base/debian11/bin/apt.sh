#!/bin/bash -eux

apt-get update
apt-get dist-upgrade --yes
apt-get autoremove --yes
apt-get clean
