# -*- coding: utf-8 -*-
import pika

# 创建连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建一个名为 hello 的队列
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='hello world')

print 'send hello world'

# 关闭连接
connection.close()


