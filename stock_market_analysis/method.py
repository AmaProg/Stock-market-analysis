import menu

from commun import utils, constants as k
from commun.answer_choice import AnswerChoice
from api_financial.fundamental_modeling_prep import FundamentalModelingPrep
from society.stock_company import Enterprise

FIRST_ELEMENT = 0

def fundamental_business_analysis():
    #Demander a l'utiliateur d'entrer le symbole qu'il veut analyser

    while True:
        user_input: str = str(input("\nVeuillez indiquer le symbole que vous voulez analysis : "))

        if(user_input.isdigit() == True):
            utils.display_error('\nLe symbole ne pas etre uniquement des chiffre.')
            continue
        
        #Verifier que le symbole est present dans la liste des marcher 
        #boursier recu de l'API Fundamental modeling Prep
        ticker_list = user_input.split(" ")
        stock_market_list = utils.read_json_file(k.STOCK_MARKET_SYMBOL_LIST_PATH)
        ticker = ticker_list[FIRST_ELEMENT]

        if(utils.is_valid_ticker(ticker, stock_market_list) == False):
            utils.display_error("Le symbole selectionner n'est pas valide. Veuillez refaire la selection")
            continue
        
        else:
            break

    #Verifier si le symbole verse des dividends dans la liste des 
    #marcher boursier pour dividend fournie par l'API Fundamental
    #modeling Prep
    dividend_stock_market_list = utils.read_json_file(k.DIVIDEND_SYMBOL_LIST_PATH)
    is_dividend_stock = False

    if(utils.is_valid_ticker(ticker, dividend_stock_market_list) == True):
        is_dividend_stock = True

    #Verifie si le symbole est present dans la base de donnee
    fmp = FundamentalModelingPrep(k.FUNDAMENTAL_MODELING_API_KEY)
    enterprise = Enterprise()
    fmp_options = {
        'profile': fmp.get_profile,
        'historical_dividend': fmp.get_historical_dividend,
        'financial_ratio': fmp.get_company_financial_ratio,
        'income_statement': fmp.get_income_statement,
        'balance_sheet': fmp.get_balance_sheet_statement,
        'cash_flow': fmp.get_cash_flow_statement
    }
    

    if(utils.path_exists(f"{k.TICKERS_PATH}/{ticker}.json") == True):

        while True:

            user_input: str = str(input(f"\nIl y a un fichier {ticker}.json qui existe deja. Voulez vous utiliser ces informations? (yes or no) : "))

            if(user_input in AnswerChoice.get_yes_choice()):
                ticker_file: dict = utils.read_json_file(f"{k.TICKERS_PATH}/{ticker}.json")

                for key in fmp_options.keys():

                    if (ticker_file.get(key) == None):
                        ticker_file[key] = fmp_options[key](ticker)
                        

                utils.write_json_file(f"{k.TICKERS_PATH}/{ticker}.json", ticker_file)
                utils.wait(0.1)
                enterprise.load(f"{k.TICKERS_PATH}/{ticker}.json")

                break

            elif(user_input in AnswerChoice.get_no_choice()):
                __build_society_stock_market(enterprise, fmp, ticker)
                break

            else:
                utils.display_error("Le choix n'est pas valide")
                continue
    else:
        __build_society_stock_market(enterprise, fmp, ticker)
            

def comparative_analysis_between_companies():
    print("comparative_analysis_between_companies")

def comparative_dividend_analysis():
    print("comparative_dividend_analysis")

def __build_society_stock_market(enterprise: Enterprise, fmp: FundamentalModelingPrep, ticker: str):
    enterprise.overview.profile = fmp.get_profile(ticker)
    enterprise.history_data.historical_dividend = fmp.get_historical_dividend(ticker)
    enterprise.financial_ratio.company_financial_ratio = fmp.get_company_financial_ratio(ticker)
    enterprise.financial_statement.income_statement.historical_income_statement = fmp.get_income_statement(ticker)
    enterprise.financial_statement.balance_sheet.historical_balance_sheet = fmp.get_balance_sheet_statement(ticker)
    enterprise.financial_statement.cash_flow.historical_cash_flow = fmp.get_cash_flow_statement(ticker)
    enterprise.to_json(f"{k.TICKERS_PATH}/{ticker}.json")