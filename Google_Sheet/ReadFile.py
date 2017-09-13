from mod_database import db_manipulation,googlefilemanipulation,googlemanipulationformation
from GoogleSheet import getgoogleinfo,getgoogleformation
# _*_ coding:utf-8 _*_



#file = open('C:\\Users\\axu30\\Desktop\\Evaluation2015-16.csv')
#db_manipulation(file)
'''
try:
## LOAD FRENCH ANSWER
    sp = "Evaluation_fr (Responses)"
    lang= 'FR'
    Division = 'DC SAS'
    procedure = "DC_SAS_EvaluationUpdate"
    output = getgoogleinfo(sp)
    googlefilemanipulation(output,lang,Division)
except:
    print("Error processing FR")

## LOAD ENGLISH ANSWER
try:
    sp = "Evaluation-en (Responses)"
    lang= 'ENG'
    Division = 'DC SAS'
    procedure = "DC_SAS_EvaluationUpdate"
    output = getgoogleinfo(sp)
    googlefilemanipulation(output,lang,Division)
except:
    print("Error processing ENG")
## LOAD GER ANSWER
try:
    sp = "Evaluation-de (Responses)"
    lang= 'GER'
    Division = 'DC SAS'
    procedure = "DC_SAS_EvaluationUpdate"
    output = getgoogleinfo(sp)
    googlefilemanipulation(output,lang,Division)
except:
    print("Error processing GER")
'''
## LOAD FORMATION
try:
    sp = "CurrentYear_Formation_Facturation"
    Division = 'DC SAS'
    procedure = "DC_SAS_FormationUpdate"
    output = getgoogleformation(sp)
    googlemanipulationformation(Division,procedure,output)
except:
    print("Error processing formation data")