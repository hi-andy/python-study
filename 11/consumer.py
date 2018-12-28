import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')



def callback(ch, method, properties, body):
    print(" [x] received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动发送处理完毕确认

channel.basic_consume(
    callback,
    queue='hello',
    # no_ack=True   # 这里不自动确认消息处理完毕，在回调函数里手动确认
)

print(" [*] Waiting for messages. To exit press Ctrl + C")

channel.start_consuming()