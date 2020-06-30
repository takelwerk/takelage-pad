#!/bin/bash

apt-get -y update
apt-get install -y --no-install-recommends python3 python3-apt systemd
apt-get clean
rm -fr /sbin/initctl
cat > /sbin/initctl <<sbin_initctl
#!/bin/sh
ALIAS_CMD="\$(echo ""\$0"" | sed -e 's?/sbin/??')"

case "\$ALIAS_CMD" in
    start|stop|restart|reload|status)
        exec service \$1 \$ALIAS_CMD
        ;;
esac

case "\$1" in
    list )
        exec service --status-all
        ;;
    reload-configuration )
        exec service \$2 restart
        ;;
    start|stop|restart|reload|status)
        exec service \$2 \$1
        ;;
    \?)
        exit 0
        ;;
esac
sbin_initctl
chmod +x /sbin/initctl
