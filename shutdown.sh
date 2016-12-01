# @Time    : 2016/12/1 11:36
# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : shutdown.sh
ps_to_kill=`ps -aux|grep vmi_server.py`
for p in $ps_to_kill do
    kill -9 `echo p|awk '{print $2}'`
done