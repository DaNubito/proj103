import os
import shutil
import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir="C:/Users/josep/OneDrive/Desktop/Project102"
to_dir="C:/Users/josep/OneDrive/Desktop/Document_Files"


list_of_files=os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name,extension)
    if extension==" ":
        continue
    if extension in [".gif.png"]:
        path1=from_dir+"/"+file_name
        path2=to_dir
        path3=to_dir+"/"+file_name
        if os.path.exists(path2):
            print("moving"+file_name)
            shutil.move(path1,path3)
        else: 
            os.makedirs(path2)
            print("moving"+file_name+".....")
            shutil.move(path1,path3)
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")
        
    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src_path}!")
    
    def on_modified(self,event):
        print(f"Hey, {event.src_path} has been modified!")

    def on_moved(self,event):
        print(f"Hey, {event.src_path} has been moved!")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
    
    