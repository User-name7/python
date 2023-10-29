#!/usr/bin/env python
# coding: utf-8

# In[110]:


import os
import shutil

path = r"C:\Users\USER\Downloads\python" # Set the path to the current working directory or specify the desired path.
file_name = os.listdir(path)  # Get a list of files in the current directory.
extensions = ["csv", "sh", "jpg"]

for file in file_name:
    file_extension = file.split('.')[-1].lower()  # Get the file extension and convert it to lowercase
    if file_extension in extensions:
        print("exist")
        if file_extension == "csv":
            destination_folder = "csv files"
        elif file_extension == "sh":
            destination_folder = "shell files"
        elif file_extension == "jpg":
            destination_folder = "image files"
        else:
            destination_folder = "other files"
        
        destination_path = os.path.join(path, destination_folder, file)
        source_path = os.path.join(path, file)

        if not os.path.exists(destination_path):
            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' to '{destination_folder}' folder.")
        else:
            print(f"'{file}' already exists in '{destination_folder}' folder.")
    else:
        print(f"Pass! '{file}' doesn't have any of the specified extensions.")



# In[ ]:





# In[ ]:




