#__author:  Administrator
#date:  2017/2/20

import pika
import sys

credentials = pika.PlainCredentials("alex","alex3714")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.0.90',credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')


result = channel.queue_declare(exclusive=True)  # exclusive=unique 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除

queue_name = result.method.queue
print("temp queue name", queue_name)

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue=queue_name,
                      )

channel.start_consuming() #以阻塞的形式接收消息