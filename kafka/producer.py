import random
from time import sleep
from json import dumps
from typing import List
import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
  bootstrap_servers=['localhost:9092'],
  value_serializer=lambda x: dumps(x).encode('utf-8'))

products = ["Romano", "X-Men", "Nivea Men", "Clear Men", "Head & Shoulders"]

# Publish text in defined topic
for e in range(100):
  ran = random.randint(30, 100)
  for i in range(ran):
    now = datetime.datetime.now()
    dt = now.strftime("%d-%m-%Y %H:%M:%S")
    prd = random.choice(products)
    data = dt + ','+ prd
    print(data)
    producer.send('First_Topic', value=data)
    sleep(ran/100)
  sleep(ran/10)

# Print message
print("Message Sent")