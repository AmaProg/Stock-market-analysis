from commun import utils, constants as k
import method as mtd

new_analysis_options = {
    1:"Effectuer une analyse fondamental d'une entreprise",
    2:"Effectuer une analyse comparatif entre entreprise",
    3:"Effectuer une analyse comparatif de dividende"
}

method_options = {
    1: mtd.fundamental_business_analysis,
    2: mtd.comparative_analysis_between_companies,
    3: mtd.comparative_dividend_analysis
}
