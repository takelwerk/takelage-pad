#!/bin/bash -eux

apt-get update
apt-get dist-upgrade
apt-get autoremove
apt-get clean
