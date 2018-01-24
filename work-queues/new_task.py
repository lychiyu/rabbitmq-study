# -*- coding: utf-8 -*-
import pika
import sys

# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建一个名为 hello 的队列
channel.queue_declare(queue='task_queue')

message = ' '.join(sys.argv[1:]) or "hello world!" 

channel.basic_publish(exchange='', routing_key='task_queue', body=message, properties=pika.BasicProperties(
        delivery_mode = 2, # 使消息持久
    ))

print 'send ' + message

# 关闭连接
connection.close()


