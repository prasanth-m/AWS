import boto3
import time
import json
import decimal

# Kinesis setup
kinesis = boto3.client("kinesis",region_name='us-east-1')
timestream = boto3.client('timestream-write')
shard_id = "shardId-000000000000" 
pre_shard_it = kinesis.get_shard_iterator(StreamName="timeseries-stream", ShardId=shard_id, ShardIteratorType="LATEST")
shard_it = pre_shard_it["ShardIterator"]
DB_NAME = 'ecomm'
TABLE_NAME = 'inventory'

def write_time_stream(records):

        try:
            result = timestream.write_records(DatabaseName=DB_NAME, TableName=TABLE_NAME,
                                              Records=records, CommonAttributes={})
         #   print("Write Status: [%s]" % result['ResponseMetadata']['HTTPStatusCode'])
        except Exception as err:
            print("Error:", err)

while True:
	out = kinesis.get_records(ShardIterator=shard_it, Limit=10)
	for record in out['Records']:
		#print (record)
		records  = []
		data = json.loads(record['Data'])
		records.append(data)
		write_time_stream(records)
	shard_it = out["NextShardIterator"]
	time.sleep(1.0)