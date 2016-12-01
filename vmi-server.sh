# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : vmi-server.sh
# This script will be add to /etc/init.d/
start() {
        echo "Starting vmi-server"
        cd /root/vmi-server
        ./startup.sh
}
stop() {
         echo "Starting vmi-server"
        cd /root/vmi-server
        ./shutdown.sh
}