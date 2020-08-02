#!/usr/bin/env bash

jq -r '.users.admin.password' {{ takel_takelpad_lib }}/settings.json
