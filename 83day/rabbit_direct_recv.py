#__author:  Administrator
#date:  2017/2/20

import pika,sys
'''组播'''
credentials = pika.PlainCredentials("alex","alex3714")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.0.90',credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue


severities = sys.argv[1:] #可以输入多个级别，info warning error
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:#[info, warning ,error ]
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(callback,queue=queue_name)

channel.start_consuming()