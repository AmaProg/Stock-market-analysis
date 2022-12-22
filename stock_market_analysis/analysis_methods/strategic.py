
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
    # old_ticker = []
    # new_ticker = []
    ticker_dict = {}
    
    #Cette boucle for verifier dans le dossier data si les entreprise 
    #selectionner par l'utilisateur n'ont pas deja ete evaluer.
    for i in range(0, len(ticker_list)):
        ticker = ticker_list[i]
        
        if(utils.path_exists(f"{k.DATA_PATH}/{ticker}.json") == True):
            while True:
                user_input = str(input(f"\nVoulez vous recuperer le ticker {ticker} existant pour cette analyse? (Y, N) : "))
                
                if(user_input.lower() in AnswerChoice.get_yes_choice()):
                    #old_ticker.append(ticker)
                    ticker_dict[ticker] = RECOVER_TICKER
                    break
                elif(user_input.lower() in AnswerChoice.get_no_choice()):
                    #new_ticker.append(ticker)
                    ticker_dict[ticker] = NEW_TICKER
                    break
                else:
                    print("\nLa valeur entrer doit etre Y ou N")
                    utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
                    continue
        else:
            #new_ticker.append(ticker)
            ticker_dict[ticker] = -1
            
    if(RECOVER_TICKER in ticker_dict.values()):
        new_dividend_analysis(ticker_dict)
    
    
    #fundamental_analysis(ticker_list)
            
    
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
            enterprise.to_json(f"{k.DATA_PATH}/{ticker}.json")
            #enterprise.to_json("app/analysis/dividend_strategic", Strategic.DIVIDEND_STRATEGIC)
            utils.wait(0.5)
            
            bar()
            
def fundamental_analysis(ticker_list:list):
    header_enterprise = 'Entreprise'
    header_ticker = 'Ticker'
    header_growth_eps = 'Croiss. BPA (%)'
    header_eps = "BPA ($)"
    header_growth_div = 'Croiss. Div (%)'
    header_annual_div = 'Div Annuel ($)'
    header_share_price = 'Prix action ($)'
    header_rendement = 'Rendement (%)'
    header_growth_estimate = "Croiss. estimer (%)"
    header_note = 'Performance (%)'
    header_distribution_income = 'Distribution Profit (%)'
    header_dividend_aristocrats = 'Aristocrat dividend'

    header=[header_enterprise, 
            header_ticker, 
            header_growth_eps,
            header_eps,
            header_growth_div,
            header_annual_div,
            header_share_price,
            header_rendement,
            header_growth_estimate,
            header_note,
            header_distribution_income,
            header_dividend_aristocrats
            ]

    #dividend_table = pd.DataFrame(columns=header)
    
    number_element = len(ticker_list)
    data = []
    ent = Enterprise()
    with alive_bar(number_element) as bar:
        for i in range(0, number_element):
            ticker = ticker_list[i]
            ticker_data = {}
            
            #Lecture des ticker dans la liste et recuperation des informations
            # db_file = open(f"app/analysis/dividend_strategic/{ticker}.bin","rb")
            # ent = pickle.load(db_file)
            # db_file.close()
            
            json_data = utils.read_json_file(f"{k.DATA_PATH}/{ticker}.json")
            
            ent.overview.profile = json_data['profile']
            ent.history_data.historical_dividend = json_data['historical_dividend']
            
            #ent = read_file(f"app/analysis/dividend_strategic/{ticker}.bin", ticker)
            
            utils.wait(0.250)
            
            ticker_data = {
                header_enterprise: ent.company_name,
                header_ticker: ent.symbol,
                header_growth_eps: 0,
                header_eps: 0,
                header_growth_div: 0,
                header_annual_div: ent.annual_dividend,
                header_share_price: 0,
                header_rendement: 0,
                header_growth_estimate: 0,
                header_note: 0,
                header_distribution_income: 0,
                header_dividend_aristocrats: False,
            }
            
            data.append(ticker_data)
            
            bar()
    utils.write_json_file("database/analysis_dividend.json", data)
    #Save_enterprise_on_bin_file("database",data,"analyse_dividend")