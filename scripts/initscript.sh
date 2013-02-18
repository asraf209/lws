#!/bin/bash
#lws
#description: startup script for lws

case $1 in
    start)
        /bin/bash /etc/lws/scripts/client/start.sh
    ;;
    stop)
        /bin/bash /etc/lws/scripts/client/stop.sh
    ;;
    restart)
        /bin/bash /etc/lws/scripts/client/start.sh
        /bin/bash /etc/lws/scripts/client/stop.sh
    ;;
esac

