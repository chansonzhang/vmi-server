#!/bin/bash
#startup.sh
#@author Zhang Chen
kill -9 `ps -aux|grep vmi_server.py|awk 'NR==1{print $2}'`
nohup python vmi_server.py &