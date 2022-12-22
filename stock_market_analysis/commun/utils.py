import os

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