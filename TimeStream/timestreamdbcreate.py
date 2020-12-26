import boto3

client = boto3.client('timestream-write', region_name='us-east-1'))

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