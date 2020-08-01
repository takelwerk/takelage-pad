#!/usr/bin/env bash

ETHERPAD_IP=$(ip --json address | jq -r '.[-1].addr_info[0].local')
ETHERPAD_ADMIN_PASSWORD=$({{ takel_etherpad_bin }}/etherpad-admin-password-get)
MYSQL_ETHERPAD_USER=$(grep user {{ takel_etherpad_home }}/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
MYSQL_ETHERPAD_PASSWORD=$(grep password {{ takel_etherpad_home }}/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
MYSQL_ROOT_USER=$(grep user /root/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
MYSQL_ROOT_PASSWORD=$(grep password /root/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')

echo "etherpad address: $ETHERPAD_IP"
if [ "$1" == "secrets" ]; then
  echo "etherpad admin user: admin"
  echo "etherpad admin password: $ETHERPAD_ADMIN_PASSWORD"
  echo "mysql etherpad user: $MYSQL_ETHERPAD_USER"
  echo "mysql etherpad password: $MYSQL_ETHERPAD_PASSWORD"
  echo "root etherpad user: $MYSQL_ROOT_USER"
  echo "root etherpad password: $MYSQL_ROOT_PASSWORD"
fi
