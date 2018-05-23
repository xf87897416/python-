#__author:  Administrator
#date:  2017/2/20

import pika
import sys

credentials = pika.PlainCredentials("alex","alex3714")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.0.90',credentials=credentials))
channel = connection.channel()


channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info' #严重程度
message = ' '.join(sys.argv[2:]) or 'Hello World!'


channel.basic_publish(exchange='direct_logs',
                      routing_key=severity, #把消息发送到指定一组队列里
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()