# _*_coding:utf-8_*_
__author__ = 'Alex Li'
import pika,time

credentials = pika.PlainCredentials("alex","alex3714")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.0.90',credentials=credentials))
channel = connection.channel()


def callback(ch, method, properties, body):
    #print(ch, method, properties, body)
    print(" [x] Received %r" % body)
    time.sleep(10)
    print(" [x] Done")
    print("method.delivery_tag", method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)  #确认消息收到


channel.basic_qos(prefetch_count=1) #类似权重，按能力分发，如果有一个消息，就不在给你发

channel.basic_consume(callback,
                      queue='task_queue2',
                      # no_ack=True    默认是消息持久化开启后，会丢失
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()