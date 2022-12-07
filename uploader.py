from azure.storage.blob import BlobServiceClient;
from azure.storage.blob import ContentSettings;
from azure.core.exceptions import ResourceExistsError;
import os;
from multiprocessing.pool import ThreadPool;
import uuid;
import shutil;


STORAGE_ACCOUNT_KEY = " ";
STORAGE_ACCOUNT_NAME = " ";
CON_STR = " ";
LOCAL_PATH = r" ";

class AzureBlobUploader:
    
    CONTAINER_NAME = "";
    blob_service_client = "";
    
    def __init__(self):
        self.blob_service_client = BlobServiceClient.from_connection_string(CON_STR);
        self.CONTAINER_NAME = str(uuid.uuid1());
        
        try:
            new_container = self.blob_service_client.create_container(self.CONTAINER_NAME);
            properties = new_container.get_container_properties();
        except ResourceExistsError:
            print("Container already exists.");
        print("intializing uploader");
        
    def run(self,all_file_names):
        with ThreadPool(processes=int(5)) as pool:
            return pool.map(self.upload_image, all_file_names);
  
    def upload_all_images_in_folder(self):
        
      all_file_names = [f for f in os.listdir(LOCAL_PATH)
                    if os.path.isfile(os.path.join(LOCAL_PATH, f)) and ".jpg" in f]
      self.run(all_file_names);
      
    def upload_image(self, file_name):
        blob_client = self.blob_service_client.get_blob_client(container = self.CONTAINER_NAME, blob = file_name)
        upload_file_path = os.path.join(LOCAL_PATH, file_name)
        
        image_content_setting  = ContentSettings(content_type = 'image/jpeg');
        print(f"uploading file- {file_name}");
        
        with open(upload_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite = True, content_settings = image_content_setting);
            
    def deleteLocDir(self):
        
        for files in os.listdir(LOCAL_PATH):
            path = os.path.join(LOCAL_PATH, files);
        try:
            shutil.rmtree(path);
        except OSError:
            os.remove(path);
            
     