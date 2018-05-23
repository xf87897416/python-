#__author:  Administrator
#date:  2017/2/20

import pika
import sys
'''广播'''
credentials = pika.PlainCredentials("alex","alex3714")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.0.90',credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout')


message = ' '.join(sys.argv[1:]) or "info: Hello World!"
print(sys.argv[1:],'===')
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()



