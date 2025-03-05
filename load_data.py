import json
from azure.cosmos import CosmosClient

# Cosmos DB credentials
endpoint = "https://tomicosmosdbdemo.documents.azure.com:443/"
key = "EblxzNm3uL5PZVxTeHlmdEHJdyVjKrFlxBYIjbNTPjHg2vg9nhArjydGWMQIoNOtZDxJqqyCwiNWACDb32ngVQ=="
client = CosmosClient(endpoint, key)

# Connect to database & container
database_name = 'TomiDB'
container_name = 'TomiContainer'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Insert data by hardcoding
products = [
    {"id": "101", "name": "Smartphone", "price": 299.99, "category": "Electronics", "stock": 50},
    {"id": "102", "name": "Laptop", "price": 799.99, "category": "Electronics", "stock": 30},
    {"id": "103", "name": "Headphones", "price": 49.99, "category": "Accessories", "stock": 100}
]

# Insert data to database
for product in products:
    container.upsert_item(product)

print(f"Inserted {len(products)} products into Cosmos")
