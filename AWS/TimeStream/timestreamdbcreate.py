import boto3

client = boto3.client('timestream-write')

response = client.create_database(
    DatabaseName='ecomm',
    Tags=[
        {
            'Key': 'db',
            'Value': 'ts_ecomm'
        },
    ]
)

print(response)