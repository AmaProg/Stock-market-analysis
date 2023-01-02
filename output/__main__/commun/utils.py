import os
import json

from time import sleep

def display_title(title: str):
    print(f"""
          ##########################################################################################
          
                                        {title.upper()}       
          
          ##########################################################################################
          """)
def wait(time_to_wait):
    sleep(time_to_wait)
    
def path_exists(path):
   return os.path.exists(path)

def read_json_file(json_file):
    with open(json_file,"r") as file:
        json_data = json.load(file)

    return json_data

def write_json_file(path: str, data):
    json_string = json.dumps(data, indent=2)

    with open(path, 'w') as outfile:
        outfile.write(json_string)