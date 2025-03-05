from azure.cosmos import CosmosClient

# Cosmos DB credentials
endpoint = "https://tomicosmosdbdemo.documents.azure.com:443/"
key = "EblxzNm3uL5PZVxTeHlmdEHJdyVjKrFlxBYIjbNTPjHg2vg9nhArjydGWMQIoNOtZDxJqqyCwiNWACDb32ngVQ=="
client = CosmosClient(endpoint, key)

# Create database and container
database_name = 'TomiDB'
container_name = 'TomiContainer'

# Create Database if it doesn't exist, checking
database = client.create_database_if_not_exists(database_name)

# Create Container if it doesn't exist, checking
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key={'paths': ['/id'], 'kind': 'Hash'},
    offer_throughput=400
)

print(f"Database '{database_name}' and Container '{container_name}' created or already exist.")
