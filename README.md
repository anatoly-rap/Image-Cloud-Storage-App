# Image-Cloud-Storage-App
A small project to get familiar with Azure, blob-storage
Will require a blob storage account, and USB stick



Populate a config.yml with these fields. When the watchdog script is launched, it will wait for a USB device to be connected.
It will look for config.yml, then extract the fields, launching the python script with the variables as args.
This way, the plaintext Azure storage account key, name, and connection string are never stored in the program when not in use. 

```
azure:
  storage_account_key: "YOUR_STORAGE_ACCOUNT_KEY"
  storage_account_name: "YOUR_STORAGE_ACCOUNT_NAME"
  connection_string: "YOUR_CONNECTION_STRING"

```
This means that people with different Azure accounts can securely connect with this application, without having to go in and manually populate the variable fields. 
