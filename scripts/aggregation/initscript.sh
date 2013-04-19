#!/bin/bash
#lws
#description: startup script for lws

case $1 in
    start)
        /bin/bash /etc/lws/scripts/aggregation/start.sh
    ;;
    stop)
        /bin/bash /etc/lws/scripts/aggregation/stop.sh
    ;;
    restart)
        /bin/bash /etc/lws/scripts/aggregation/start.sh
        /bin/bash /etc/lws/scripts/aggregation/stop.sh
    ;;
esac

