import os
import time
import datetime
import pypyodbc as pyodbc
import csv

def pushoutputfiles():
    ####################################
    ## Read and Insert Methodes
    ####################################

    def insertlist (cursor,list,command):
        for newinfo in list:
            cursor.execute(command, (newinfo[0], newinfo[1], newinfo[2],
                                           newinfo[3], newinfo[4], newinfo[5],
                                           newinfo[6], newinfo[7], newinfo[8],
                                           newinfo[9], newinfo[10], newinfo[11],
                                           newinfo[12], newinfo[13]))
            cursor.commit()


    def createlist (account,division):
        with open("C:\\Users\\AXU30\\Documents\\GitHub\\Python\\Python-request\\UbityETL\\file\\outgoing-%s-2017-%s.csv" % (
        account, '%02d' % month)) as file:
            next(file)
            result = list()
            for temp in file:
                res=temp.split(',')
                line =  (division, #Division
                        cleanse(res[0]), #Call Date - Date
                        cleanse(res[5]), #Call Identifier - To
                        "Outbound", #QueueName
                        cleanse(res[3]), #Agent - From Extension
                        cleanse(res[1]), #Action - State
                        None, #KeyPressed
                        None, #Position
                        None, #WaitTime
                        convertfloats(res[6]), #Call Time - Duration
                        None, #OriginalPosition
                        tsform,#CreateDate
                        None, #FinishCall_Reason
                        None, #Language
                        )
                result.append(line)
        return result

    ##################################
    #### Get SQL connection
    ##################################

    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=dc-a-slsql;DATABASE=BI;UID=BI_User;PWD=BI_User')
    cursor = conn.cursor()


    def closecursor(cursor):
        cursor.close()

    ################################
    #### Cleaning Functions
    ################################
    def convertfloats (x):
        clean=x.replace('"',"")
        number=float(clean)
        return number

    def cleanse (x):
        clean=x.replace('"',"")
        return clean

    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    ts =time.time()
    tsform = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    result03 = createlist('dis0003','DC INC')
    #result06 = createlist('dis0006','DC SAS')

    ############################
    ### Insert info in DB
    ###########################

    deletecommand = """DELETE FROM T_Ubity_caller_queue WHERE
                       YEAR(CreateDate) = ? AND MONTH(CreateDate) = ?
                       AND QueueName='Outbound'"""

    cursor.execute(deletecommand,(year,month))

    insertcommand = """INSERT INTO T_Ubity_caller_queue VALUES (?,?,?,?,?,?,?,?,
                                                                ?,?,?,?,?,?)"""

    insertlist(cursor,result03,insertcommand)
    #insertlist(cursor,result06,insertcommand)

    closecursor(cursor)





