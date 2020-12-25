# Collect and Store Streaming TimeSeries data into Amazon TimeStream DB

## Please note

This repository has fully functional streaming setup which can stream, collect and write timeseries data in to target TimeStream DB, the objective is to provide basic idea of how to collect and store Time Series data in to Amazon Timestream.The performance and other aspects of aws services were not considered while creating these gists. 


## Prerequisites

> Python3.X with dependent modules

> IAM role and other AWS access permissions


## How to RUN

Create a lambda function , deploy and schedule them to run as per the timeseries events window

Create Amazon TimeStream DB and table

```
python timestreamdbcreate.py
python timestreamtablecreate.py
```

## Databases

<b>Amazon TimeStream : </b> TimeStream is used to store all the timeseries data

## Compute
<b>AWS Lambda: </b> Lambda is used to read data from kinesis and to write data in to TimeStream DB

## Streaming
<b>Amazon Kinesis: </b> Kinesis is used to stream the ordered TimeSeries data


## Dependent Libraries

### Boto3 : https://pypi.org/project/boto3/
