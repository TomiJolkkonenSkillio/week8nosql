from azure.cosmos import CosmosClient
import statistics

# Cosmos DB credentials
endpoint = "https://tomicosmosdbdemo.documents.azure.com:443/"
key = "EblxzNm3uL5PZVxTeHlmdEHJdyVjKrFlxBYIjbNTPjHg2vg9nhArjydGWMQIoNOtZDxJqqyCwiNWACDb32ngVQ=="
client = CosmosClient(endpoint, key)

# Connect to database & container
database_name = 'TomiDB'
container_name = 'TomiContainer'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Query all products
query = "SELECT * FROM c"
items = container.query_items(query, enable_cross_partition_query=True)

# Calculate mean, max, and min prices
prices = [product['price'] for product in items]
mean_price = statistics.mean(prices)
max_price = max(prices)
min_price = min(prices)

print(f"Mean Price: {mean_price}")
print(f"Max Price: {max_price}")
print(f"Min Price: {min_price}")
