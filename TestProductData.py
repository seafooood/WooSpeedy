import json
import unittest
from ProductData import ProductData

class TestProductData(unittest.TestCase):

    def test_toJson(self):

        # Arrange 
        p1 = ProductData()
        p1.name = "apple"
        p1.sku = "fruit1"
        p1.regular_price = 0.50
        p1.description = "Lovely green apple"
        p1.short_description = "green apple"
        p1.category_id = 1
        p1.images_url = ["apple1.png", "apple2.png", "apple2.png"]
        p1.downloads_url = ["apple1.pdf", "", ""]

        expected_dict = {
            'categories': [{'id': 1}],
            'description': 'Lovely green apple',            
            'downloadable': True,
            'downloads': [],
            'images': [],
            'name': 'apple',            
            'regular_price': 0.50,
            'short_description': 'green apple',
            'sku': 'fruit1',
            'virtual' : True,            
        }

        # Act
        p1Json = p1.toJson()

        # Assert
        self.assertEqual(json.dumps(p1Json, sort_keys=True), json.dumps(expected_dict, sort_keys=True))

if __name__ == '__main__':
    unittest.main()
