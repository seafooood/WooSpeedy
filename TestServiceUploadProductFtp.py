from ServiceUploadProductFtp import GenerateUrl
import unittest

class TestGenerateUrl(unittest.TestCase):

    def test_generate_url(self):
        # Arrange
        baseUrl = "https://example.com"
        remoteDirectory = "remote"
        newFolderName = "folder"
        localFile = "file.txt"
        
        # Act
        url = GenerateUrl(baseUrl, remoteDirectory, newFolderName, localFile)

        # Assert
        expected_url = "https://example.com/remote/folder/file.txt"
        self.assertEqual(url, expected_url)

    def test_generate_url_extra_slash(self):
        # Arrange
        baseUrl = "https://example.com"
        remoteDirectory = "remote/"
        newFolderName = "/folder"
        localFile = "file.txt"
        
        # Act
        url = GenerateUrl(baseUrl, remoteDirectory, newFolderName, localFile)

        # Assert
        expected_url = "https://example.com/remote/folder/file.txt"
        self.assertEqual(url, expected_url)


if __name__ == '__main__':
    unittest.main()
