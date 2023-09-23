from configparser import ConfigParser
from ServiceCreateProduct import CreateProduct
from ServiceExistingProducts import GetExistingProducts
from ServiceReadProductData import ReadCsvAndReturnProducts
from ServiceUploadProductFtp import Uploads

def BulkUploadProducts(config, productFile):
    
    print(f"Loading product data from file {productFile}")
    products = ReadCsvAndReturnProducts(productFile)
    print(f"Found {len(products)} in file {productFile}")

    print("Downloading exisiting product SKU data")
    existingProducts = GetExistingProducts(config)

    for product in products:
        if product.sku in existingProducts:
            print(f"Skipping product {product.name} because the SKU {product.sku} already exisits")
            continue
        
        print(f"Uploading product {product.name}")
        product.images_url = Uploads(config, product.images, config.get('folder', 'folder_product_images'), product.sku)
        product.downloads_url = Uploads(config, product.downloads, config.get('folder', 'folder_product_files'), product.sku)
        CreateProduct(config, product)
        print(f"Uploaded product {product.name}")
    pass

def AskQuestion(queston, defaultAnswer):
    answer = input(f"Enter the address of the product CSV file [{defaultAnswer}]:")
    if answer == "":
        answer = defaultAnswer
    return answer
    pass

if __name__ == "__main__":
    print("=== Starting WooSpeedy ===")
    
    # Load configuration
    config = ConfigParser()
    config.read('config.ini')

    # Ask User Questions
    productFile = AskQuestion("Enter the address of the product CSV file", f"{config.get('product', 'product_file')}")

    # Start Upload
    BulkUploadProducts(config, productFile)
    
    print("=== Finished ===")