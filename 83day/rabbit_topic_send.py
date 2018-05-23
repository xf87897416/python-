#__author:  Administrator
#date:  2017/2/20

import pika,sys
'''模糊匹配'''
credentials = pika.PlainCredentials("alex","alex3714")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.14.47',credentials=credentials))
channel = connection.channel()


channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'

message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()