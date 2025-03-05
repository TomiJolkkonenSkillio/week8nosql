import statistics
from azure.cosmos import CosmosClient

# Initialize Cosmos client and get the container
endpoint = "<your-cosmos-db-endpoint>"
key = "<your-cosmos-db-primary-key>"
client = CosmosClient(endpoint, key)
database_name = "ProductsDB"
container_name = "ProductsContainer"
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Query to retrieve all products (as a list)
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

# Query to filter products by price range (price between 20 and 50)
price_range_query = "SELECT * FROM c WHERE c.price >= 20 AND c.price <= 50"
filtered_products = container.query_items(price_range_query, enable_cross_partition_query=True)

print("\nProducts in the price range 20 to 50:")
for product in filtered_products:
    print(product)

# Query to sort products by price in descending order
sort_query = "SELECT * FROM c ORDER BY c.price DESC"
sorted_products = container.query_items(sort_query, enable_cross_partition_query=True)

print("\nSorted products by price (descending):")
for product in sorted_products:
    print(product)

# Query to group products by category and calculate average price per category
aggregation_query = """
    SELECT c.category, AVG(c.price) as avg_price 
    FROM c 
    GROUP BY c.category
"""
aggregated_results = container.query_items(aggregation_query, enable_cross_partition_query=True)

print("\nAverage price per category:")
for result in aggregated_results:
    print(f"Category: {result['category']}, Average Price: {result['avg_price']}")

# Query to count the number of products with a price greater than 50
count_query = "SELECT COUNT(1) FROM c WHERE c.price > 50"
count_result = container.query_items(count_query, enable_cross_partition_query=True)
print(f"\nCount of products with price > 50: {list(count_result)[0]['$1']}")

# Query to find products in a specific category (e.g., "Electronics")
category_query = "SELECT * FROM c WHERE c.category = 'Electronics'"
category_products = container.query_items(category_query, enable_cross_partition_query=True)

print("\nProducts in the 'Electronics' category:")
for product in category_products:
    print(product)

# Query to limit results to top 5 most expensive products
limit_query = "SELECT TOP 5 * FROM c ORDER BY c.price DESC"
limited_products = container.query_items(limit_query, enable_cross_partition_query=True)

print("\nTop 5 most expensive products:")
for product in limited_products:
    print(product)

# Query to find products whose name contains 'phone' (case-insensitive search)
search_query = "SELECT * FROM c WHERE CONTAINS(c.name, 'phone')"
search_results = container.query_items(search_query, enable_cross_partition_query=True)

print("\nProducts with 'phone' in the name:")
for product in search_results:
    print(product)

# Query to find products that are out of stock (assuming 'stock' attribute exists)
out_of_stock_query = "SELECT * FROM c WHERE c.stock = 0"
out_of_stock_products = container.query_items(out_of_stock_query, enable_cross_partition_query=True)

print("\nOut of stock products:")
for product in out_of_stock_products:
    print(product)

# Query to find the most expensive product in each category
max_price_query = """
    SELECT c.category, MAX(c.price) as max_price 
    FROM c 
    GROUP BY c.category
"""
max_price_results = container.query_items(max_price_query, enable_cross_partition_query=True)

print("\nMost expensive product in each category:")
for result in max_price_results:
    print(f"Category: {result['category']}, Max Price: {result['max_price']}")
