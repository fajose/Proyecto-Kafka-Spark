import requests
from kafka import KafkaProducer
import time
import json

endpoint = "https://api.stackexchange.com/2.3/questions"
params = {
    "pagesize": "100",
    "order": "desc",
    "sort": "activity",
    "site": "stackoverflow"
}

# Set Kafka producer properties
kafka_topic = "stackOverflow"
kafka_bootstrap_servers = ["localhost:9092"]
kafka_producer = KafkaProducer(
    bootstrap_servers=kafka_bootstrap_servers,
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Continuously retrieve new questions and send them to Kafka
while True:
    # Retrieve questions from API
    response = requests.get(endpoint, params=params)
    questions = response.json()["items"]
    
    # Send questions to Kafka
    for question in questions:
        kafka_producer.send(kafka_topic, value=question)
        
        # Sleep for a certain amount of time before retrieving new questions
        time.sleep(10)
