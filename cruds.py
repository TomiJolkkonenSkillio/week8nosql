from azure.cosmos import CosmosClient

# Replace with your Cosmos DB details
endpoint = "https://tomicosmosdbdemo.documents.azure.com:443/"
key = "EblxzNm3uL5PZVxTeHlmdEHJdyVjKrFlxBYIjbNTPjHg2vg9nhArjydGWMQIoNOtZDxJqqyCwiNWACDb32ngVQ=="
client = CosmosClient(endpoint, key)

# Connect to database & container
database_name = 'TomiDB'
container_name = 'TomiContainer'
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# CREATE (CRUD): Insert new product
def create_product(product):
    container.upsert_item(product)
    print(f"Product '{product['name']}' created")

# READ (CRUD): Get product by ID
def read_product(product_id):
    try:
        product = container.read_item(item=product_id, partition_key=product_id)
        print(f"Product Found: {product}")
        return product
    except Exception as e:
        print(f"Product not found. Error: {str(e)}")
        return None

# UPDATE (CRUD): Update existing product
def update_product(product_id, updated_fields):
    try:
        product = container.read_item(item=product_id, partition_key=product_id)
        product.update(updated_fields)
        container.replace_item(item=product, id=product_id)
        print(f"Product '{product_id}' updated")
    except Exception as e:
        print(f"Error updating product. Error: {str(e)}")

# DELETE (CRUD): Delete product ID
def delete_product(product_id):
    try:
        container.delete_item(item=product_id, partition_key=product_id)
        print(f"Product '{product_id}' deleted")
    except Exception as e:
        print(f"Error deleting product. Error: {str(e)}")

# main
if __name__ == "__main__":
    # Create product
    new_product = {
        "id": "101",  # Unique product ID
        "name": "OnePlusNord",
        "price": 299.99,
        "category": "Electronics",
        "stock": 50
    }
    create_product(new_product)
    
    # Read product
    read_product("101")
    
    # Update product
    update_product("101", {"price": 249.99, "stock": 60})
    
    # Delete product
    delete_product("101")
