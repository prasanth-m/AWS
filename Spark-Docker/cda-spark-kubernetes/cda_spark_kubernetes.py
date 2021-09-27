from pyspark.sql import SparkSession
from pyspark.sql.types import *
import sys
import os

if __name__ == "__main__" :

 s3_bucket = sys.argv[1]
 s3_prefix_input = sys.argv[2]
 s3_prefix_output = sys.argv[3]
 aws_region = sys.argv[4]
 aws_access_key_id = sys.argv[5]
 aws_secret_access_key = sys.argv[6]

 input_path = f's3a://{s3_bucket}/{s3_prefix_input}'
 output_path = f's3a://{s3_bucket}/{s3_prefix_output}'

 spark = SparkSession.builder.appName("cda-spark-delta-demo") \
 .config("spark.hadoop.fs.s3a.access.key", aws_access_key_id) \
 .config("spark.hadoop.fs.s3a.secret.key", aws_secret_access_key) \
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
 