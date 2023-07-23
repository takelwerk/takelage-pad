#!/usr/bin/env bash

VERSION_FILE={{ takel_etherpad_version_file }}
if test -f "$VERSION_FILE"; then
  VERSION=$(head -n 1 "$VERSION_FILE")
  HEADER="takelpad: $VERSION"
fi

echo "$HEADER | for details run: vagrant ssh -c takelpad"

if [ ! -z "$1" ]; then
  IP_ETHERPAD="$1"
else
  IP_ETHERPAD=$(ip --json address | jq -r '.[-1].addr_info[0].local')
fi
echo "takelpad ip address: $IP_ETHERPAD"

echo
echo "example pad urls (de):"
gopass pwgen --one-per-line --xkcd --xkcdsep - --xkcdlang de | parallel echo https://$IP_ETHERPAD/etherpad/p/{}
echo
echo "example pad urls (en):"
gopass pwgen --one-per-line --xkcd --xkcdsep - --xkcdlang en | parallel echo https://$IP_ETHERPAD/etherpad/p/{}

if [ "$1" != "--summary" ]; then
  IP_ADDRESSES=$(ip --json address | jq -r '.[].addr_info[0].local' | grep -v null)
  ETHERPAD_ADMIN_PASSWORD=$(sudo {{ takel_etherpad_bin }}/etherpad-admin-password-get)
  MYSQL_ETHERPAD_USER=$(sudo grep user {{ takel_etherpad_home }}/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
  MYSQL_ETHERPAD_PASSWORD=$(sudo grep password {{ takel_etherpad_home }}/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
  MYSQL_ROOT_USER=$(sudo grep user /root/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
  MYSQL_ROOT_PASSWORD=$(sudo grep password /root/.my.cnf | sed -e 's/.*"\([^"]*\)"/\1/')
  SSL_FINGERPRINT=$(openssl x509 -in /etc/ssl/certs/ssl.pem -noout -fingerprint)

  echo
  echo "box ip addresses:"
  echo $IP_ADDRESSES | tr " " "\n"
  echo
  echo "etherpad admin user: admin"
  echo "etherpad admin pass: $ETHERPAD_ADMIN_PASSWORD"
  echo
  echo "mysql etherpad user: $MYSQL_ETHERPAD_USER"
  echo "mysql etherpad pass: $MYSQL_ETHERPAD_PASSWORD"
  echo
  echo "mysql root user: $MYSQL_ROOT_USER"
  echo "mysql root pass: $MYSQL_ROOT_PASSWORD"

  if [ -d "/home/vagrant" ]; then

    echo
    echo "start box:   vagrant up"
    echo "stop box:    vagrant halt"
    echo "destroy box: vagrant destroy"
    echo "update box:  vagrant box update --box takelwerk/takelpad"
    echo
    echo "login user: vagrant ssh"
    echo "login root: vagrant ssh -c 'sudo su -'"
    echo
    echo "ssl fingerprint: $SSL_FINGERPRINT"
    echo "ssl check: openssl s_client -connect $IP_ETHERPAD:443  < /dev/null 2>/dev/null | openssl x509 -fingerprint -noout -in /dev/stdin"
  fi
fi
