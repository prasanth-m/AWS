import sys
from kafka import  KafkaConsumer
from kafka import TopicPartition
import boto3
import datetime
import json

KAFKATOPIC = "autofleet"
IOTTOPIC = 'connectedcar/shadow'
IOTCLIENT = boto3.client('iot-data', region_name='us-east-1')
def lambda_handler(event, context):
 if 'topic' in event:
  consumer = KafkaConsumer(bootstrap_servers='b-1.msk.u02y4o.c5.kafka.us-east-1.amazonaws.com:9094,b-2.msk.u02y4o.c5.kafka.us-east-1.amazonaws.com:9094',
                          security_protocol='SSL',
                           ssl_check_hostname=True,
                           ssl_certfile='client_cert.pem',
                           ssl_keyfile='private_key.pem',
                           ssl_cafile='truststore.pem')

  parts = consumer.partitions_for_topic(KAFKATOPIC)
  if parts is None:
   exit(1)
  partitions = [TopicPartition(KAFKATOPIC, p) for p in parts]
  consumer.assign(partitions)
  for  partition in partitions:
  consumer.seek_to_beginning(partition) #sample read. use offset
  for msg in consumer:
  val = json.loads(msg.value.decode('utf-8'))
  if val.get("value") == 'P0406':
    try:
        msg = {}
        msg['signal'] = 'stop'
        msg['module '] = 'PCM'
        msg['vin'] = val.get("vin")
        msg['timestamp'] = str(datetime.datetime.utcnow())
        print(msg)
        iottopic = '{}/{}'.format(IOTTOPIC, val.get("vin"))
        response = IOTCLIENT.publish(topic=iottopic, qos=0, payload=json.dumps(msg))
        print(response)
    except Exception as e:
        print("An error occurred on iot topic side:", e)
  else:
    pass