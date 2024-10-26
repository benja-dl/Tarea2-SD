from confluent_kafka import Consumer

consumer_conf = {
    'bootstrap.servers': 'localhost:9093',
    'group.id': 'grupo-consumidor1',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_conf)

consumer.subscribe(['pedidos'])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print("Error del consumidor: {}".format(msg.error()))
        else:
            print(f"Pedido recibido: key={msg.key().decode('utf-8')}, value={msg.value().decode('utf-8')}")

finally:
    consumer.close()
