# @Time    : 2016/12/1 11:36
# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : shutdown.sh
pids=`ps -aux|grep vmi_server.py|awk '{print $2}'`
for pid in $pids
do
    kill -9 $pid
done