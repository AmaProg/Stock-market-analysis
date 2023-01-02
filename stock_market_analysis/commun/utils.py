import os
import json
import pandas as pd

from time import sleep
from commun import constants as k
from alive_progress import alive_bar

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

def display_menu(options: dict):

    for num, option in options.items():
        print(f'{num}. {option}')

def display_error(msg_error: str):

    print(f"\n{msg_error}\n")
    wait(k.TIME_TO_DISPLAY_ERROR_MSG)

def create_folder(path: str):
    os.mkdir(path)

def check_ticker_in_stock_market_list(ticker: str, symbol_list) -> bool:
    df = pd.DataFrame(symbol_list)

    with alive_bar(len(df), dual_line=True, title=f"Validation du symbole {ticker}") as bar:
        for index, row in df.iterrows():
            if(ticker.upper()==row["symbol"]):
                print(f"{ticker} is found !")
                is_present = True
                break
                
            bar()

    return is_present

def is_valid_ticker(ticker: str, dividend_symbol_list) -> bool:
    df = pd.DataFrame(dividend_symbol_list)
    is_present = False

    with alive_bar(len(df), dual_line=True, title=f"Validation du symbole {ticker}") as bar:
        for index, row in df.iterrows():
            if(ticker.upper()==row["symbol"]):
                print(f"{ticker} is found !")
                is_present = True
                break
                
            bar()

    return is_present

def is_valid_tickers(ticker: str, stock_market_list: dict):
    return ticker in stock_market_list