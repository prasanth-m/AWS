from pyspark.sql import SparkSession
from pyspark.sql.types import *
import sys
import os

def lambda_handler(event, context):

 s3_bucket = os.environ['s3_bucket'] 
 s3_prefix_input = os.environ['inp_prefix']
 s3_prefix_output = os.environ['out_prefix']
 aws_region = os.environ['AWS_REGION'] 
 aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'] 
 aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'] 
 session_token = os.environ['AWS_SESSION_TOKEN']

 input_path = f's3a://{s3_bucket}/{s3_prefix_input}'
 output_path = f's3a://{s3_bucket}/{s3_prefix_output}'

 spark = SparkSession.builder \
 .appName("cda-spark-delta-demo") \
 .master("local[*]") \
 .config("spark.driver.bindAddress", "127.0.0.1") \
 .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id) \
 .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key) \
 .config("spark.hadoop.fs.s3a.session.token",session_token) \
 .config("spark.hadoop.fs.s3a.aws.credentials.provider","org.apache.hadoop.fs.s3a.TemporaryAWSCredentialsProvider") \
 .config("fs.s3a.endpoint", "s3-ap-south-1.amazonaws.com") \
 .getOrCreate()
 
 print("***************start***********")
 
 df = spark.read.format('csv').option('header','true').option('inferSchema','true').load('%s' % input_path)
 df.show()
 

 print("***************write delta***********")

 df.write.format("delta").mode("append").save("%s" % output_path)
 spark.sql("CREATE TABLE events USING DELTA LOCATION '%s'" % output_path)
 
 print("***************read delta***********")

 df_delta=spark.read.format("delta").load("%s" % output_path)  # query table by path
 df_delta.show()
 
 spark.stop()
 return "Finally, spark on AWS lambda completed !!!"