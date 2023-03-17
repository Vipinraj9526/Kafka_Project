# Kafka_Project
##This project completely about kafka
- Step 1

to start zookeeper 
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties


to stop zookeeper 
.\bin\windows\zookeeper-server-stop.bat

- step 2
- 
to start broker 
.\bin\windows\kafka-server-start.bat .\config\server.properties


to stop broker 
.\bin\windows\kafka-server-stop.bat

- step3
- 
to create topic 
.\bin\windows\kafka-topics.bat --create --topic firstTopic --bootstrap-server localhost:9092 
.\bin\windows\kafka-topics.bat --create --topic secondTopic --bootstrap-server localhost:9092 
.\bin\windows\kafka-topics.bat --create --topic thirdTopic --bootstrap-server localhost:9092 


topic creation with partition and replication factor 
.\bin\windows\kafka-topics.bat --create --topic thirdTopic --partitions 1 --replication-factor 1 --bootstrap-server localhost:9092 

to get the topic details and information 
.\bin\windows\kafka-topics.bat --bootstrap-server localhost:9092 --describe --topic thirdTopic

to delete topic 
.\bin\windows\kafka-topics.bat --delete --topic thirdTopic --bootstrap-server localhost:9092 


to list all topics 
.\bin\windows\kafka-topics.bat --list --bootstrap-server localhost:9092


- step 4
to start producer 
.\bin\windows\kafka-console-producer.bat --topic firstTopic --bootstrap-server localhost:9092 
.\bin\windows\kafka-console-producer.bat --topic secondTopic --bootstrap-server localhost:9092 


-step 5
to start consumer 

.\bin\windows\kafka-console-consumer.bat --topic firstTopic --from-beginning --bootstrap-server localhost:9092 
.\bin\windows\kafka-console-consumer.bat --topic secondTopic --from-beginning --bootstrap-server localhost:9092 


.\bin\windows\kafka-console-consumer.bat --topic firstTopic --bootstrap-server localhost:9092 

to get consumer group 
.\bin\windows\kafka-consumer-groups.bat --bootstrap-server localhost:9092 
