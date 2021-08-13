from threading import current_thread
from time import time
from typing import Union
from pyspark import SparkConf, SparkContext
import datetime
from json import dumps
from kafka import KafkaProducer
conf = SparkConf().setAppName('KafkaStreaming')
sc = SparkContext(conf=conf)
from pyspark.streaming import StreamingContext 
from pyspark.streaming.kafka import KafkaUtils 
ssc = StreamingContext(sc, 30) 

brokers = "localhost:9092" 
topic = "First_Topic" 

def str_x (x):
    length = len(x)
    n = length-1
    return x[0:n] 

def printx (x):
    print(x[0] + ": " + str(x[1]))

def sendPartition(iter):
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8'))
    for record in iter:
        data = '{' + '"bike_name":"' + record[0] + '","total":' + str(record[1]) + ',"date_time":"' + record[2] + '"}'
        producer.send('Second_Topic', value = data)
    producer.close()

stream = KafkaUtils.createDirectStream \
(ssc, [topic], {"metadata.broker.list": brokers}) 
lines = stream.map(lambda x: x[1]) 
counts = lines.map(lambda x: x.split(",")) \
              .map(lambda x: (str_x(x[1]),1)) \
              .reduceByKey(lambda x, y: x + y)
                       
counts.pprint()
counts.foreachRDD(lambda x: x.map(lambda x: (x[0],x[1], datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))).foreachPartition(sendPartition))  

ssc.start() 
ssc.awaitTermination()