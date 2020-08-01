#!/usr/bin/env bash

jq -r '.users.admin.password' {{ takel_etherpad_lib }}/settings.json
