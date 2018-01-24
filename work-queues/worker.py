# -*- coding: utf-8 -*-

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

def callback(ch, method, properties, body):
    print "receive "+ body
    time.sleep(body.count(b'.'))
    print "done"


channel.basic_consume(callback, queue='task_queue', no_ack=True)

# 开始无限循环接收消息
channel.start_consuming()

