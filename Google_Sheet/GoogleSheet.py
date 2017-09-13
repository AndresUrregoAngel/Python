# _*_ coding:utf-8 _*_
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def getgoogleinfo(SpreadSheet):
    scope =['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('distech-c1e26e7150b2.json',scope)
    gc = gspread.authorize(credentials)

    spreadsheet = gc.open(SpreadSheet)
    wks = spreadsheet.worksheet('Form Responses 1')

    #out = wks.col_values(1)
    #out2 = wks.get_all_records(empty2zero=False, head=1, default_blank='')
    out2 = wks.get_all_values()

    return out2



def getgoogleformation(SpreadSheet):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('distech-c1e26e7150b2.json', scope)
    gc = gspread.authorize(credentials)

    spreadsheet = gc.open(SpreadSheet)
    wks = spreadsheet.worksheet('Suivi_Facturation')

    # out = wks.col_values(1)
    # out2 = wks.get_all_records(empty2zero=False, head=1, default_blank='')
    out2 = wks.get_all_values()

    return out2
