# @Time    : 2016/11/14 15:11
# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : vmi_server.py.py

#!/usr/local/bin/python
import pika
from oslo_log import log
import subprocess

LOG = log.getLogger(__name__)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')


def get_process_list(instance_name):
    command = "vol.py -l vmi://" + instance_name + " --profile=LinuxCentos7-3_10_0-327_36_3_el7_x86_64x64 linux_pslist"
    LOG.debug('Command: %(command)s',
              {'command': command})
    out = ''
    try:
        out = subprocess.check_output("export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH && " + command,
                                      shell=True).decode('utf-8')
    except subprocess.CalledProcessError as e:
        out_bytes = e.output  # Output generated before error
        code = e.returncode  # Return code
        LOG.error(
            "Error when get process, the output generated before error:%(out_bytes)s, the return code is %(return_code)s",
            {'out_bytes': out_bytes,
             'return_code': code})

    LOG.debug('Out: %(out)s',
              {'out': out})
    return out

def on_request(ch, method, props, body):
    instance_name = str(body)
    response = get_process_list(instance_name)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

LOG.info(" [x] Awaiting RPC requests")
channel.start_consuming()