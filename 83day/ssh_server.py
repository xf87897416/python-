#__author:  Administrator
#date:  2017/2/20

import pika,sys
import subprocess


credentials = pika.PlainCredentials("alex","alex3714")

connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.14.47',credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue='rpc_queue')


def CMD(cmd):

    cmd_obj = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    cmd_result = cmd_obj.stdout.read() +  cmd_obj.stderr.read()

    return cmd_result

def on_request(ch, method, props, body):

    print(" [.]recv cmd(%s)" % body)
    response = CMD(body)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()