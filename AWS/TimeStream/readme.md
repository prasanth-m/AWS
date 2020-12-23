# Serverless Streaming Timeseries Data Collection for AMAZON Timestream

## Please note

While the gist of this repository has fully functional streaming setup which can stream timeseries data and write in to target TimeStream DB, the objective is to provide basic idea of how to collect and store Time Series data in to AMAZON Timestream


## Prerequisites

> Python3.X with dependent modules

> I AM role and other AWS access permissions


## How to RUN

Create lambda function , deploy and schedule to run

Create Kinesis Data Streams

```
python3 stream_ws.py
````

Create Amazon TimeStream DB

```
python stream_ws.py
```

## Databases

<b>AMAZON TimeStream : </b> TimeStream is used to store all the timeseries data

## Compute
<b>AWS Lambda: </b> Lambda is used to read from kinesis and write data in to TimeStream DB

## Streaming
<b>Amazon Kinesis: </b> Kinesis is used to stream the ordered TimeSeries data

Make sure you've <b>dependencies</b> installed ahead as per requirements.txt


## Dependent Libraries

### Boto3 : https://pypi.org/project/boto3/
