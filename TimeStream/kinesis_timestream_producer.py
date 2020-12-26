import boto3
import json
import random
import time

my_stream_name = 'timeseries-stream'

kinesis_client = boto3.client('kinesis', region_name='us-east-1')

def put_to_stream(inventory, price, recorded_time):
   
    payload = {
         'MeasureValue': str(price),
         'MeasureName': 'qty', 
         'MeasureValueType': 'DOUBLE', 
         'Dimensions': [{
                        'Name': 'inventory', 
                        'Value': str(inventory)
                        }],
         'Time': str(recorded_time)
        }


    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=inventory)
   # print(put_response)

while True:
    price = random.randint(1000, 1100)
    recorded_time = str(int(round(time.time() * 1000)))
    inventory = 'phone'
    put_to_stream(inventory, price, recorded_time)

    # wait for 5 second
    time.sleep(1)