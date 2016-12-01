# @Time    : 2016/12/1 11:44
# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : create-service-and-run.sh

chmod a+x vmi-server
cp vmi-server /etc/init.d/
cd /etc/init.d/
chkconfig --add vmi-server
chkconfig vmi-server on
service restart vmi-server.service