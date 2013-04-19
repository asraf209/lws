#!/bin/bash

sudo python /home/paulie/lws/client/lws_server_main_zeromq.py <&- 1>/dev/null 2>&1 &
pid=$!
sudo echo ${pid} > /var/run/lwsserver.pid
echo "the pid is" $pid
