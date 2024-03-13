# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:09:26 2024

@author: adon.augustin
"""

import time
import shutil
import os

def get_folder_size(path):
    total_size=0
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_folder_size(entry.path)
    return total_size
    


x=time.time()
source='C:/Users/adon.augustin/Documents/BenPower/React/hmi-compressor-copy/'
destination='Z:/WeekleyBackup/React1/hmi-compressor-backup/'
new_path=""
if os.path.exists(destination): #make a copy of  folder
    dest_new=destination.split('/')
    dest_new[len(dest_new)-2]=dest_new[len(dest_new)-2]+"_copy"
    for i in dest_new:
        new_path+=str(i+"/")
    try:
        shutil.copytree(source,new_path) #then copy files to folder
    except:
        print("error")
    if(get_folder_size(new_path)==get_folder_size(source)):  #check for any lost memmory
        try:
            shutil.rmtree(destination)
        except OSError as e:
            print(f"print folder deletion failed {e}")
        try:
            os.rename(new_path,destination) #rename the new_path by old path
        except:
            print("Error in renaming folder")
    else:
        print("Memmory copy issue")
else:
    try:
        shutil.copytree(source,destination)
    except:
        print("error")
y=time.time()
t=y-x
print("seconds taken is",t)