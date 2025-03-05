import requests
from azure.cosmos import CosmosClient

# Initialize Cosmos client and get the container
endpoint = "<your-cosmos-db-endpoint>"
key = "<your-cosmos-db-primary-key>"
client = CosmosClient(endpoint, key)
database_name = "ProductsDB"
container_name = "ProductsContainer"
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Fetch and insert data from the API (for i = 1 to 100)
for i in range(1, 101):
    url = f"https://dummyjson.com/products/{i}"  # Fetch product with ID i
    response = requests.get(url)
    
    if response.status_code == 200:
        product = response.json()
        # Insert product data into the container
        container.upsert_item(product)
        print(f"Inserted product {i}")
    else:
        print(f"Failed to fetch product {i}")

print("Finished loading products!")
