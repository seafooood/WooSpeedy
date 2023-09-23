from configparser import ConfigParser
import requests
import json

def GetExistingProducts(config):
    # Construct the URL for the API request
    api_url = config.get('store', 'store_base_url')
    endpoint = '/wp-json/wc/v3/products'
    url = f'{api_url}{endpoint}'

    # Set up authentication
    auth = requests.auth.HTTPBasicAuth(config.get('store', 'store_consumer_key'), config.get('store', 'store_consumer_secret'))

    # Define query parameters (to fetch all products)
    params = {
        'per_page': 100,  # Adjust the number of products per page as needed
        'page': 1,        # Start with the first page
    }

    # List to store product SKUs
    product_skus = []

    # Fetching all product SKUs by paginating through the results
    print("Fetching all product SKUs by paginating through the results")
    while True:
        response = requests.get(url, auth=auth, params=params)

        if response.status_code == 200:
            products = json.loads(response.text)

            if not products:
                break  # No more products to fetch

            for product in products:
                product_skus.append(product['sku'])

            # Move to the next page
            params['page'] += 1
            print(f"Downloading page {params['page']} of product sku data")
        else:
            print(f"Failed to fetch products. Status code: {response.status_code}")
            break
    return product_skus

if __name__ == "__main__":
    # Example usage:
    print("=== Starting ===")
    
    # Load configuration
    config = ConfigParser()
    config.read('Config.ini')

    # Get a list existing product sku
    productSkus = GetExistingProducts(config)

    # Print the list of product SKUs
    for sku in productSkus:
        print(sku)
    
    print("=== Finished ===")
