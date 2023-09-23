import csv
from ProductData import ProductData

def ReadCsvAndReturnProducts(fileName):
    products = []

    try:
        with open(fileName, mode='r', newline='') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                product = ProductData()
                product.name = row["name"].strip('"')
                product.sku = row["sku"].strip('"')
                product.regular_price = row["regular_price"].strip('"')
                product.description = row["description"].strip('"')
                product.short_description = row["short_description"].strip('"')
                product.category_id = int(row["category_id"])
                product.images = [row["image1"].strip('"'), row["image2"].strip('"'), row["image3"].strip('"')]
                product.downloads = [row["download1"].strip('"'), row["download2"].strip('"'), row["download3"].strip('"')]
                products.append(product)

    except FileNotFoundError:
        print(f"File '{fileName}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return products

if __name__ == "__main__":
    # Example usage:
    print("=== Starting ===")
    fileName = "TestData\Products.csv"
    product_list = ReadCsvAndReturnProducts(fileName)
    for product in product_list:
        print(product.name)
        print(product.images)
        print(product.short_description)
    print("=== Finished ===")
