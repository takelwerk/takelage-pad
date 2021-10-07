#!/usr/bin/env bash

VERSION_FILE={{ takel_etherpad_version_file }}
if test -f "$VERSION_FILE"; then
  VERSION=$(head -n 1 "$VERSION_FILE")
  HEADER="takelpad: $VERSION"
fi

echo "$HEADER | for details run: vagrant ssh -c takelpad"

IP_ETHERPAD=$(ip --json address | jq -r '.[-1].addr_info[0].local')
echo "takelpad ip address: $IP_ETHERPAD"

if [ "$1" != "--summary" ]; then
  IP_ADDRESSES=$(ip --json address | jq -r '.[].addr_info[0].local')
  ETHERPAD_ADMIN_PASSWORD=$(sudo {{ takel_etherpad_bin }}/etherpad-admin-password-get)
  MYSQL_ETHERPAD_USER=$(sudo grep user {{ takel_etherpad_home }}/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
  MYSQL_ETHERPAD_PASSWORD=$(sudo grep password {{ takel_etherpad_home }}/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
  MYSQL_ROOT_USER=$(sudo grep user /root/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
  MYSQL_ROOT_PASSWORD=$(sudo grep password /root/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')

  echo
  echo "box ip addresses:"
  echo $IP_ADDRESSES | tr " " "\n"
  echo
  echo "etherpad admin user: admin"
  echo "etherpad admin password: $ETHERPAD_ADMIN_PASSWORD"
  echo
  echo "mysql etherpad user: $MYSQL_ETHERPAD_USER"
  echo "mysql etherpad password: $MYSQL_ETHERPAD_PASSWORD"
  echo
  echo "mysql root user: $MYSQL_ROOT_USER"
  echo "mysql root password: $MYSQL_ROOT_PASSWORD"
  echo
  echo "start box: vagrant up"
  echo "stop box: vagrant halt"
  echo "destroy box: vagrant destroy"
  echo
  echo "login user: vagrant ssh"
  echo "login root: vagrant ssh -c 'sudo su -'"
fi
