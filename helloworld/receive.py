# -*- coding: utf-8 -*-

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print "receive "+ body


channel.basic_consume(callback, queue='hello', no_ack=True)

# 开始无限循环接收消息
channel.start_consuming()

