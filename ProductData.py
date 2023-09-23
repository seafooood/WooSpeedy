
class ProductData:

    def __init__(self):
        pass

    name = ""
    sku = ""
    regular_price = 0
    description = ""
    short_description = ""
    category_id = 0
    images = []
    images_url = []
    downloads = []
    downloads_url = []
    
    def toJson(self):
        imageJson = []
        for i in self.images_url:
            imageJson.append({'src' : i})

        downloadJson = []
        for d in self.downloads_url:
            downloadJson.append({'name':'PDF File', 'file': d})
        
        productJson = {
            'name': self.name,
            'downloadable': True,  # Set the product as downloadable
            'virtual': True,      # Set the product as virtual
            'regular_price': self.regular_price,
            'sku': self.sku,
            'description':self.description,
            'short_description': self.short_description,
            'categories': [{'id': 1}],
            'images' : imageJson,
            'downloads': downloadJson
        }
        
        return productJson
        pass

if __name__ == "__main__":
    # Example usage:
    print("=== Starting ===")

    p1 = ProductData
    p1.name = "apple"
    p1.sku= "fruit1"
    p1.regular_price = 0.50
    p1.description = "Lovely green apple"
    p1.short_description = "green apple"
    p1.category_id = 1
    p1.images = ["apple1.png", "apple2.png", "apple2.png"]
    p1.downloads = ["apple1.pdf"]

    p1Json = p1.toJson(p1)
    print(p1Json)

    print("=== Finished ===")
