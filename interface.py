import shutil
import tkinter as tk
from tkinter import *
from uploader import AzureBlobUploader;
from tkinter import messagebox, filedialog
import os;
	
def CreateWidgets():
    
	link_Label = Label(root, text ="Select The File To Copy: ",bg = "#E8D579");
	link_Label.grid(row = 1, column = 0,pady = 5, padx = 5);
	root.sourceText = Entry(root, width = 50,textvariable = sourceLocation);
	root.sourceText.grid(row = 1, column = 1,pady = 5, padx = 5,columnspan = 2);
	source_browseButton = Button(root, text ="Browse",command = SourceBrowse, width = 15);
	source_browseButton.grid(row = 1, column = 3,pady = 5, padx = 5);
	copyButton = Button(root, text ="Copy File", command = CopyFile, width = 15);
	copyButton.grid(row = 3, column = 1,pady = 5, padx = 5);
	moveButton = Button(root, text ="Move File",command = MoveFile, width = 15);
	moveButton.grid(row = 3, column = 2,pady = 5, padx = 5);

def SourceBrowse():
	root.files_list = list(filedialog.askopenfilenames(initialdir = os.path.expanduser('~')));
	root.sourceText.insert('1', root.files_list)
	
def GetDestination():
	destinationdirectory = "images_tests";
	return destinationdirectory;
	
def CopyFile():
	files_list = root.files_list
	destination_location = GetDestination();
	for f in files_list:
		shutil.copy(f, destination_location);
	messagebox.showinfo("files have been uploaded.")
	
def MoveFile():
	files_list = root.files_list
	destination_location = GetDestination();
	for f in files_list:
		shutil.move(f, destination_location);
	messagebox.showinfo("upload successful");

root = tk.Tk();
root.geometry("600x100");
root.title("AzCloud Uploader");
root.config(background = "#e0e0eb");
sourceLocation = StringVar();
CreateWidgets();
root.mainloop();
blob_uploader = AzureBlobUploader();
blob_uploader.upload_all_images_in_folder();
blob_uploader.deleteLocDir();