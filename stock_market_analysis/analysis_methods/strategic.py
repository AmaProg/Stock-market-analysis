
from commun import constants as k, utils, answer_choice
from commun.answer_choice import AnswerChoice
from society.stock_company import Enterprise
from api_financial.fundamental_modeling_prep import FundamentalModelingPrep
from alive_progress import alive_bar

#----- personnal constants -----
RECOVER_TICKER=-1
NEW_TICKER=1
#----- end personnal constants


def dividend_strategic(ticker_list : list) -> list:
    ticker_dict = {}
    
    #Cette boucle for verifier dans le dossier data si les entreprise 
    #selectionner par l'utilisateur n'ont pas deja ete evaluer.
    for i in range(0, len(ticker_list)):
        ticker = ticker_list[i]
        
        if(utils.path_exists(f"{k.TICKERS_PATH}/{ticker}.json") == True):
            while True:
                user_input = str(input(f"\nVoulez vous recuperer le ticker {ticker} existant pour cette analyse? (Y, N) : "))
                
                if(user_input.lower() in AnswerChoice.get_yes_choice()):
                    ticker_dict[ticker] = RECOVER_TICKER
                    break
                
                elif(user_input.lower() in AnswerChoice.get_no_choice()):
                    ticker_dict[ticker] = NEW_TICKER
                    break
                
                else:
                    print("\nLa valeur entrer doit etre Y ou N")
                    utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
                    continue
        else:
            ticker_dict[ticker] = NEW_TICKER
            
    if(NEW_TICKER in ticker_dict.values()):
        new_dividend_analysis(ticker_dict)
            
    
def new_dividend_analysis(new_ticker_dict: dict):

    fmp = FundamentalModelingPrep(k.FUNDAMENTAL_MODELING_API_KEY)
    number_element = len(new_ticker_dict)
    
    with alive_bar(number_element, dual_line=True, title='Recuperation des donnee') as bar:

        for ticker in new_ticker_dict.keys():

            enterprise = Enterprise()

            if(new_ticker_dict[ticker] == RECOVER_TICKER):
                continue
            
            #obtenir l'appercu de l'entreprise
            enterprise.overview.profile = fmp.get_profile(ticker)
            enterprise.history_data.historical_dividend = fmp.get_historical_dividend(ticker)
            enterprise.financial_ratio.company_financial_ratio = fmp.get_company_financial_ratio(ticker)
            enterprise.financial_statement.income_statement.historical_income_statement = fmp.get_income_statement(ticker)
            enterprise.to_json(f"{k.TICKERS_PATH}/{ticker}.json")
            utils.wait(0.100)
            
            bar()