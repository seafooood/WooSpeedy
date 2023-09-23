from configparser import ConfigParser
from urllib.parse import urljoin
import paramiko
import os

def Uploads(config, localFilePaths, remoteDirectory, newFolderName):
    remoteUrls = []
    OpenConnection(config)
    CreateProductFolder(remoteDirectory, newFolderName)
    for localFilePath in localFilePaths:
        url = Upload(config, localFilePath, remoteDirectory, newFolderName)
        if url != "":
            remoteUrls.append(url)
    CloseConnection()
    return remoteUrls
    pass


def OpenConnection(config):
    global ssh, sftp

    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the SFTP server
    ssh.connect(config.get('sftp', 'sftp_host'), config.get('sftp', 'sftp_port'), config.get('sftp', 'sftp_user'), config.get('sftp', 'sftp_pass'))

    # Create an SFTP session
    sftp = ssh.open_sftp()
    pass

def CreateProductFolder(remoteDirectory, newFolderName):
    global sftp

    # Change the current directory to the remote directory
    sftp.chdir(remoteDirectory)

    # Create the new folder (if it doesn't exist)
    try:
        sftp.mkdir(newFolderName)
    except IOError:
        pass  # Folder already exists

    # Change the current directory to the new folder
    sftp.chdir(newFolderName)
    pass

def CloseConnection():
    global ssh, sftp
    # Close the SFTP session and SSH connection
    sftp.close()
    ssh.close()
    pass
    

def Upload(config, localFilePath, remoteDirectory, newFolderName):
    if localFilePath is None or localFilePath == "":
        print("WARNING: Skipping empty file")
        return ""

    print(f"Uploading file {localFilePath}")
    if os.path.isfile(localFilePath) == False:
        print(f"Error: File '{localFilePath}' does not exist")
        return ""

    # Upload the local file to the new folder
    localFolder, localFile = os.path.split(localFilePath)
    sftp.put(localFilePath, localFile)

    # Print a success message
    uploadUrl = GenerateUrl(config.get('store', 'store_base_url'), remoteDirectory, newFolderName, localFile)
    print(f"File '{localFile}' uploaded to {uploadUrl}")

    return uploadUrl
    pass

def GenerateUrl(baseUrl, remoteDirectory, newFolderName, localFile):
    baseUrl = baseUrl.rstrip('/') + '/'
    return urljoin(baseUrl, f"{remoteDirectory}/{newFolderName}/{localFile}")



if __name__ == "__main__":
    # Example usage:
    print("=== Starting ===")

    # Load configuration
    config = ConfigParser()
    config.read('config.ini')

    # Upload files
    print(Upload(config, "TestData/pear1.png", "/wp-content/uploads", "productcode123"))
    print(Upload(config, "TestData/pear1.pdf", "/wp-content/uploads/woocommerce_uploads", "productcode123"))

    print("=== Finished ===")
