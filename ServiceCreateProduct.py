from ProductData import ProductData
from configparser import ConfigParser
import requests

def CreateProduct(config, productData):
    print(f"Creating product {productData.name}")
    productJson = productData.toJson()
    print(productJson)

    auth = (config.get('store', 'store_consumer_key'), config.get('store', 'store_consumer_secret'))
    endpoint = f"{config.get('store', 'store_base_url')}/wp-json/wc/v3/products"
    response = requests.post(endpoint, auth=auth, json=productJson)

    if response.status_code == 201:
        print("Product created successfully.")
        productId = response.json().get('id')
        print(f"Product ID: {productId}")
    else:
        print("Failed to create the product.")
        print(f"Status code: {response.status_code}")
        print(f"Error message: {response.json()}")
    pass

if __name__ == "__main__":
    # Example usage:
    print("=== Starting ===")
    
    # Load configuration
    config = ConfigParser()
    config.read('Config.ini')

    # Product details
    p1 = ProductData()
    p1.name = "apple"
    p1.sku= "fruit12"
    p1.regular_price = '0.50'
    p1.description = "Lovely green apple"
    p1.short_description = "green apple"

    # Create Product
    CreateProduct(config, p1)
        
    print("=== Finished ===")