from commun.answer_choice import AnswerChoice
from commun import utils, constants as k
from economic import analysis 

def run():
    f"""
        Cette fonction {run} demarre l'application principale.
    """

    run_app = True

    #Demande a l'utilisateur s'il veut faire une nouvelle analyse ou arreter l'application
    while True:

        if(run_app == True):
            my_app()

        user_input = str(input("\nVoulez vous effectuer une autre analyse? (yes/no): "))

        if (user_input.lower() in AnswerChoice.get_yes_choice()):
            run_app = True
            continue
        elif(user_input.lower() in AnswerChoice.get_no_choice()):
            print("Fin du programme")
            break
        else:
            print("\nLa touche n'est pas valide.")
            run_app = False
            continue

def my_app():

    utils.display_title("Debut d'Analyse fondamentale")
    
    # Demander a l'utilisateur quel type d'analyse veut il faire
    #   1. Analyse par cycle economie du pays (cycle economie)
    #   2. Analyse par comparaison d'entreprise (comparaison d'entreprise)
    while True:
        try:
            print("1. Analyse par cycle economique")
            print("2. Analyse par comparaison d'entreprise\n")
    
            ans = int(input("Quel type d'analyse voulez vous faire (1 ou 2) : "))
            
            if(ans <= 0 or ans > 2):
                print("\nLe choix doit etre 1 ou 2\n")
                utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
                continue
            
        except ValueError:
            print("\nVotre choix n'est pas valide \n")
            utils.wait(k.TIME_TO_DISPLAY_ERROR_MSG)
            continue
        
        else:
            break
    
    
    if(ans == 1):
        #Si 1 choisi appeler la fonction analyse par cycle economie
        analysis.economic_cycle_analysis()
    elif(ans == 2):
        #Si 2 choisi appeler la fonction analyse par comparaison        analysis_by_comparison()
        analysis.analysis_by_comparison()
    else:
        print('Aucune analyse est possible')