#__author:  Administrator
#date:  2017/2/16

import pika
import sys,time

credentials = pika.PlainCredentials("alex","alex3714")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.0.90',credentials=credentials))

channel = connection.channel()

# 声明queue
channel.queue_declare(queue='task_queue2',durable=True) #队列持久化 服务器重启就没了

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.

message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()
channel.basic_publish(exchange='',
                      routing_key='task_queue2',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent# 消息持久化
                      )
                      )
print(" [x] Sent %r" % message)
connection.close()