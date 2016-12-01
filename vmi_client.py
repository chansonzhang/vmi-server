# @Time    : 2016/11/14 15:22
# @Author  : Zhang Chen
# @Email    : zhangchen.shaanxi@gmail.com
# @File    : vmi_client.py

#!/usr/local/bin/python
import pika
import uuid

class VMIRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
                host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, instance_name):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         correlation_id = self.corr_id,
                                         ),
                                   body=str(instance_name))
        while self.response is None:
            self.connection.process_data_events()
        return str(self.response)

vmi_rpc = VMIRpcClient()

instance_name = "instance-00000014"
print(" [x] Requesting get_process_list(%s)",instance_name)
response = vmi_rpc.call(instance_name)
print(" [.] Got %s" % response)