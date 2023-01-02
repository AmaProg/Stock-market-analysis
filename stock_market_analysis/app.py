import menu

from commun.answer_choice import AnswerChoice
from commun import utils, constants as k

def run():
    """
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

    #Verifier si le dossier ticker est present dans la base de donnee
    if(utils.path_exists(k.TICKERS_PATH) == False):
        utils.create_folder(k.TICKERS_PATH)
    
    while True:

        utils.display_menu(menu.new_analysis_options)

        try:
            ans = int(input("\nQuel type d'analyse voulez vous faire : "))
            
        except ValueError:
            utils.display_error("Le choix doit etre un nombre entre 1 et 3.")
            continue

        if(ans in menu.method_options):
            menu.method_options[ans]()
            break
        else:
            utils.display_error("Votre choix n'est pas valide")


