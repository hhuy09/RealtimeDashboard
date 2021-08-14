"# RealtimeDashboard" 
![image](https://user-images.githubusercontent.com/53387573/129353303-74c09a2a-c5ad-441e-8624-14db652917d8.png)
## OS: Wndowns
## Apache Spark spark-2.3.2-bin-hadoop2.6 (Spark Streaming)
## Apache Kafka kafka_2.12-2.8.0
Create topics: Fisrt_Topic & Second_Topic
1. kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic First_Topic
2. kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic Second_Topic
## Python 3.6.8
Package         Version
--------------- -------
findspark       1.4.2
kafka           1.3.5
kafka-python    2.0.2
pip             18.1
psutil          5.8.0
py4j            0.10.7
pyparsing       2.4.7
pyspark         2.4.6
python-dateutil 2.8.2
pytz            2021.1
setuptools      40.6.2
six             1.16.0
## Nodejs
npm init

npm install --save express

npm install --save socket.io

npm install --save nodemon

npm install --save kafka-node

## Run System
1. Start zookepper: zookeeper-server-start.bat %KAFKA_HOME%\config\zookeeper.properties
2. Start server-kafka:kafka-server-start.bat %KAFKA_HOME%\config\server.properties
3. Submit consumer-streaming.py: spark-submit --master local[2] --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0 ...\consumer-streaming.py
4. Run node: nodemon server-kafka.js 
5. Access localhost:xxxx

![image](https://user-images.githubusercontent.com/53387573/129433052-2ccbafa9-248d-4819-bc51-50dc2b439679.png)

