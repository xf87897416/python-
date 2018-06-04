#__author:  Administrator
#date:  2017/2/20

import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials("alex", "alex3714")

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            '192.168.14.47', credentials=credentials))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue #定义了一个随机的rpc_result queue

        self.channel.basic_consume(self.on_response,queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None #消息接收到之后，会把结果赋值给response
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events() #以非阻塞的方式去检查有没有新消息，有的话就接收
        return self.response


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call("df -h")
print(" [.] Got cmd result" )
print(response.decode("utf-8"))