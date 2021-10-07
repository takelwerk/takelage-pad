#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 new_password"
    exit 1
fi

SETTINGS_JSON="{{ takel_etherpad_lib }}/settings.json"

jq -r --arg PASSWORD "$1" '.users.admin.password = $PASSWORD' $SETTINGS_JSON | sponge $SETTINGS_JSON
