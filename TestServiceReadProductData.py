import unittest

from ServiceReadProductData import ReadCsvAndReturnProducts
from ProductData import ProductData

class TestServiceReadProductData(unittest.TestCase):

    def test_read_valid_csv(self):
        # Arrange
        test_csv = "TestData/test.csv"
        with open(test_csv, "w") as file:
            file.write('''name,sku,regular_price,description,short_description,category_id,image1,image2,image3,download1,download2,download3
"apple","fruit1",0.50,"Lovely green apple","green apple",1,"apple1.png","apple2.png","apple2.png","apple1.pdf","",""
"orange","fruit2",0.40,"Fresh juicy orange","Juicy Orange",1,"orange1.png","orange2.png","orange2.png","orange1.pdf","",""''')
        p1 = ProductData()
        p1.name = "apple"
        p1.sku= "fruit1"
        p1.regular_price = '0.50'
        p1.description = "Lovely green apple"
        p1.short_description = "green apple"
        p1.category_id = 1
        p1.images = ["apple1.png", "apple2.png", "apple2.png"]
        p1.downloads = ["apple1.pdf", "", ""]

        p2 = ProductData()
        p2.name = "orange"
        p2.sku= "fruit2"
        p2.regular_price = '0.40'
        p2.description = "Fresh juicy orange"
        p2.short_description = "Juicy Orange"
        p2.category_id = 1
        p2.images =  ["orange1.png", "orange2.png", "orange2.png"]
        p2.downloads = ["orange1.pdf", "", ""]
        expected_result = [p1,p2]

        # Act
        products = ReadCsvAndReturnProducts(test_csv)

        # Assert 
        self.assertEqual(len(products), len(expected_result))
        for i in range(len(products)):
            self.assertEqual(products[i].name, expected_result[i].name)
            self.assertEqual(products[i].sku, expected_result[i].sku)
            self.assertEqual(products[i].regular_price, expected_result[i].regular_price)
            self.assertEqual(products[i].description, expected_result[i].description)
            self.assertEqual(products[i].short_description, expected_result[i].short_description)
            self.assertEqual(products[i].category_id, expected_result[i].category_id)
            self.assertEqual(products[i].images, expected_result[i].images)
            self.assertEqual(products[i].downloads, expected_result[i].downloads)

        # Clean up the test CSV file
        import os
        os.remove(test_csv)
        pass

    def test_read_nonexistent_csv(self):
        # Arrange
        non_existent_csv = "non_existent.csv"

        # Act
        products = ReadCsvAndReturnProducts(non_existent_csv)

        # Assert 
        self.assertEqual(products, [])
        pass

if __name__ == '__main__':
    unittest.main()
