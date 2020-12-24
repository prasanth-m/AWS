import boto3

client = boto3.client('timestream-write')

response = client.create_table(
    DatabaseName='ecomm',
    TableName='inventory',
    RetentionProperties={
        'MemoryStoreRetentionPeriodInHours': 8,
        'MagneticStoreRetentionPeriodInDays': 1
    },
    Tags=[
        {
            'Key': 'table',
            'Value': 'ecomm_inventory'
        },
    ]
)

print(response)