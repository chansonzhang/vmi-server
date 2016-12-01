# @Time    : 2016/12/1 11:36
# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : shutdown.sh
kill -9 `ps -aux|grep vmi_server.py|awk 'NR==1{print $2}'`