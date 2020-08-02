#!/usr/bin/env bash

ETHERPAD_ADMIN_PASSWORD=$(pwgen -s1 20)
BIN_SET_PASS="{{ takel_takelpad_bin }}/etherpad-admin-password-set"

$BIN_SET_PASS $ETHERPAD_ADMIN_PASSWORD
