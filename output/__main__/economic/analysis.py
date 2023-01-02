import pandas as pd

from commun import utils, constants as k
from analysis_methods import  strategic
from alive_progress import alive_bar
from fundamental_analysis import FundamentalAnalysis

def economic_cycle_analysis():
    print("fonction economic_cycle_analyse")
    
    
def analysis_by_comparison():
    utils.display_title("ANALYSE BY COMPARISON")
    
    #Recuperation de la liste des symbole boursier.
    symbol_list = utils.read_json_file(k.STOCK_MARKET_SYMBOL_LIST_PATH)
    
    # Demander a l'utilisateur quel type de strategique d'analyse il veux utiliser
    #   1. analyse strategique par dividend
    #   2. analyse strategique a la warren buffet
    #   3. analyse strategique a la lychn
    while True:
        try:
            print("1. analyse strategique par Dividend")
            print("2. analyse strategique a la Warren buffet")
            print("3. analyse strategique a la Lynch\n")
            
            ans = int(input("Quel type de strategie voulez vous utiliser (1, 2 ou 3) : "))
            
            if(ans <= 0 or ans > 3):
                print("\nLe choix doit etre 1, 2 ou 3\n")
                utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
                continue
            
        except ValueError:
            print("\nVotre choix n'est pas valide \n")
            utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
            continue
        
        else:
            break
        
    # Demander a l'utilisateur le nombre d'entreprise qui veut analyser
    while True:
        try:
            number_element = int(input("\nEntrer le nombre d'entreprise que voulez vous analyser : "))
        
            if(number_element < 2):
                print("Vous devez au minimum selectionner 2 element")
                utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
                continue
        
        except ValueError:
            print("\nVotre choix doit etre une valeur numerique \n")
            utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
            continue
        else:
            break
        
        
    #Verifier que l'utilisateur a bien choisi le nombre d'element comme indiquer lors du premier choix
    while True:
        ticker_list = list(map(str,input("\nEntrer les symbol des entreprises a analyser (separer par espace) : ").strip().split()))[:number_element]
        
        if(len(ticker_list) == number_element):
            break
        
        else:
            print("\nLe nombre d'element entrer dans la liste, ne match pas avec votre choix")
            utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
            continue
        
    # Cette section verifie si les symbole boursier choisi par l'utilisateur fond partie de la liste 
    # fournie par fundament modeling prep
    while True:
        #Convertir la liste des symboles en dataframe
        df = pd.DataFrame(symbol_list)
        bad_ticker_list = []
        
        
        #Verifier les ticker selectionner s'il sont present dans la liste de fondamental mondeling prep
        for i in range(0, number_element):
            ticker = ticker_list[i]
            is_present = False
            
            with alive_bar(len(df), dual_line=True, title=f"Validation du symbole {ticker}") as bar:
                for index, row in df.iterrows():
                    if(ticker.upper()==row["symbol"]):
                        print(f"{ticker} is found !")
                        is_present = True
                        break
                        
                    bar()
            
            if(is_present == False):
                bad_ticker_list.append(ticker)
                
        if(len(bad_ticker_list) != 0):
            bad_symbole_selected(number_element, f"les symboles suivante : {bad_ticker_list} ne sont pas valide")
            continue
        
        #Cette section permet de verifier si les symboles selectionner par l'utilisateur verse des dividends.
        if(ans == 1):
            is_valid = _check_ticker_dividend(ticker_list)
            
            if(is_valid == True):
                break
            else:
                print(f"les symboles suivante : {bad_ticker_list} ne sont pas des entreprise qui verse des dividend")
                utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
                ticker_list = list(map(str,input("\nEntrer les symbol des entreprises a analyser (separer par espace) : ").strip().split()))[:number_element]
                continue
    
    #----- choix 1 -----
    # Appeler la fonction dividend_strategique
    if(ans == 1):
        
        strategic.dividend_strategic(ticker_list)

        fa = FundamentalAnalysis(ticker_list)
        
        fa.build_dividend_strategy_table()
    
    # ----- choix 2 -----
    elif(ans == 2):
        print('warren buffet strategie')
        
    # ----- choix 3 -----
    elif(ans == 3):
        print("Lynch strategie")
        
    else:
        print("Impossible d'effectuer une analyse")
        
def _check_ticker_dividend(ticker_list : list) -> bool: 
    
    dividend_symbol_list = utils.read_json_file(k.DIVIDEND_SYMBOL_LIST)
    number_element = len(ticker_list)
    bad_ticker_list = []
    
    #Converir le fichier json en dataframe
    df = pd.DataFrame(dividend_symbol_list)
    

    for i in range(0, number_element):
        ticker = ticker_list[i]
        is_present = False
        
        with alive_bar(len(df), dual_line=True, title=f"Validation du symbole {ticker}") as bar:
            for index, row in df.iterrows():
                if(ticker.upper() == row['symbol']):
                    print(f"{ticker} is found")
                    is_present = True
                    break
                
                bar()
                
        if(is_present == False):
            bad_ticker_list.append(ticker)
            
    if(len(bad_ticker_list) == 0):
        return True
    
    else:
        return False

def bad_symbole_selected(number_element: int, msg: str):
    f"""
        La function {bad_symbole_selected} permet de reposer la meme question lorsque l'utilisateur 
        ne choisi pas les bon symbole bousier ou les symbole des entreprise qui verse des dividendes
    """

    print(msg)

    utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)

    ticker_list = list(map(str,input("\nEntrer les symbol des entreprises a analyser (separer par espace) : ").strip().split()))[:number_element]

    return ticker_list