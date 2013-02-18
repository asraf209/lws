#!/bin/bash

python /etc/lws/client/lws_client_main.py <&- 1>/dev/null 2>&1 &
pid=$!
echo ${pid} > /var/run/lwsclient.pid
echo "the pid is" $pid
