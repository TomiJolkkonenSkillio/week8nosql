from azure.cosmos import CosmosClient, PartitionKey

# Set up Cosmos DB credentials
endpoint = "<your-cosmos-db-endpoint>"  # Replace with your Cosmos DB endpoint
key = "<your-cosmos-db-primary-key>"    # Replace with your Cosmos DB key

# Initialize Cosmos client
client = CosmosClient(endpoint, key)

# Create a new database (if it doesn't exist)
database_name = "ProductsDB"
database = client.create_database_if_not_exists(id=database_name)

# Create a new container (if it doesn't exist)
container_name = "ProductsContainer"
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/category"),  # Partition key based on 'category'
    offer_throughput=400  # You can adjust the throughput (performance) of the container
)

print(f"Database '{database_name}' and container '{container_name}' are created!")
