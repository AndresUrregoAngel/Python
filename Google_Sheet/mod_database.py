# _*_ coding:utf-8 _*_
import sqlite3
import pyodbc
import datetime

now = datetime.datetime.now()

def odbconnection():
    conn = pyodbc.connect( 'DRIVER={SQL Server};'
                       'SERVER=DC-A-SLSQL;'
                       'DATABASE=BI;'
                       'UID=BI_User;'
                       'PWD=BI_User;'
                       )
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor

def sqliteconnection():
    connection = sqlite3.connect("survey.dbf")
    cursorlite = connection.cursor()
    #connection.autocommit = True
    return cursorlite

def closecursor(connection):
    connection.close()

#this procedure if just invoked to load flat files
def db_manipulation(file):

    cursorlite.execute(
        """ CREATE TABLE IF NOT EXISTS questions (
        ID INTEGER ,
        Question_N TEXT,
        Answer TEXT
        )
        """
        )
    connection.commit()

    cursorlite.execute(
        """ CREATE TABLE IF NOT EXISTS survey (
        ID INTEGER,
        Division TEXT,
        Language TEXT,
        Create_Date TEXT ,
        Event_Date TEXT,
        Training_program TEXT,
        Trainer_name TEXT,
        Last_Name TEXT,
        Name TEXT,
        Company TEXT,
        mail TEXT,
        Role TEXT,
        Cellphone TEXT,
        Telephone TEXT,
        Comments TEXT,
        Comments_1 TEXT,
        Comments_2 TEXT,
        global_satisfaction,
        nps_eu TEXT,
        nps TEXT
        )
        """
        )
    connection.commit()


    cmd_truncate_questions = 'delete from questions'
    cmd_truncate_survery  ='delete from survey'
    cmd_insert_questions = 'INSERT INTO questions VALUES (?,?,?)'
    cmd_insert_survey = 'INSERT INTO survey VALUES (?,?,?,?,?,?,?' \
                           ',?,?,?,?,?,?,?,?,?,?,?,?,?)'
    #cmd_select_questions = 'SELECT * FROM questions'
    #cmd_select_survey = 'SELECT * FROM survey'
    cmd_joinoutput = 'SELECT a.*,b.* FROM survey a LEFT JOIN questions b ON a.ID=b.ID'
    cmd_prod_insert = 'INSERT INTO T_SAS_Historical_Evaluation VALUES(?,?,?,?,?,?,?,?' \
                      ',?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

    cursorlite.execute(cmd_truncate_questions)
    cursorlite.execute(cmd_truncate_survery)
    next(file)
    i = 42
    for line in file:
        res = line.split(';')
        cursorlite.execute(cmd_insert_survey,(i,"DC SAS",res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7],
                                              res[8], res[9], res[10], res[11], res[22], res[28],
                                              res[34],res[35],res[36],res[37]))

        cursorlite.execute(cmd_insert_questions, (i, "Q1", res[12]))
        cursorlite.execute(cmd_insert_questions, (i, "Q2", res[13]))
        cursorlite.execute(cmd_insert_questions, (i, "Q3", res[14]))
        cursorlite.execute(cmd_insert_questions, (i, "Q4", res[15]))
        cursorlite.execute(cmd_insert_questions, (i, "Q5", res[16]))
        cursorlite.execute(cmd_insert_questions, (i, "Q6", res[17]))
        cursorlite.execute(cmd_insert_questions, (i, "Q7", res[18]))
        cursorlite.execute(cmd_insert_questions, (i, "Q8", res[19]))
        cursorlite.execute(cmd_insert_questions, (i, "Q9", res[20]))
        cursorlite.execute(cmd_insert_questions, (i, "Q10", res[21]))
        cursorlite.execute(cmd_insert_questions, (i, "Q11", res[23]))
        cursorlite.execute(cmd_insert_questions, (i, "Q12", res[24]))
        cursorlite.execute(cmd_insert_questions, (i, "Q13", res[25]))
        cursorlite.execute(cmd_insert_questions, (i, "Q14", res[26]))
        cursorlite.execute(cmd_insert_questions, (i, "Q15", res[27]))
        cursorlite.execute(cmd_insert_questions, (i, "Q16", res[29]))
        cursorlite.execute(cmd_insert_questions, (i, "Q17", res[30]))
        cursorlite.execute(cmd_insert_questions, (i, "Q18", res[31]))
        cursorlite.execute(cmd_insert_questions, (i, "Q19", res[32]))
        cursorlite.execute(cmd_insert_questions, (i, "Q20", res[33]))
        connection.commit()
        i += 1

    cursorlite.execute(cmd_joinoutput)
    resultq1 = cursorlite.fetchall()


    for line in resultq1:
        cursor.execute(cmd_prod_insert,(line[0],line[1],line[2],line[3],
                                        line[4],line[5],line[6],line[7],
                                        line[8],line[9],line[10],line[11],
                                        line[12],line[13],line[14],line[15],
                                        line[16],line[21],line[22],line[17],line[18],line[19]
                                        ,now))
        conn.commit()
        #print(line,now)


def googlefilemanipulation(infolist,lang,Division):

## Open cursor
    cursor =  odbconnection()
    cursorlite = sqliteconnection()
##Queries Library
    cmd_getcurrentid = 'SELECT cast(id as int)  FROM  T_SAS_Historical_Evaluation ORDER BY Id DESC'
    cmd_clean_survey = 'delete from survey'
    cmd_clean_questions = 'delete from questions'
    cmd_insert_questions = 'INSERT INTO questions VALUES (?,?,?)'
    cmd_insert_survey = 'INSERT INTO survey VALUES (?,?,?,?,?,?,?' \
                        ',?,?,?,?,?,?,?,?,?,?,?,?,?)'
    cmd_select_questions = 'SELECT * FROM questions'
    cmd_select_survey = ("SELECT * FROM survey WHERE Create_Date IS NOT '' ")
    cmd_prod_insert = 'INSERT INTO T_SAS_Staging_Evaluation VALUES(?,?,?,?,?,?,?,?' \
                      ',?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    cmd_prod_cleaning_staging = "TRUNCATE TABLE T_SAS_Staging_Evaluation"
    cmd_prod_executesp = 'exec DC_SAS_EvaluationUpdate ?'
### Execute each cursor to clean up the local tables and set counter

    cursor.execute(cmd_getcurrentid)
    cursorlite.execute(cmd_clean_questions)
    cursorlite.execute(cmd_clean_survey)

### Start counter
    a= cursor.fetchone()
    i = a[0]+1
## Get the final output to insert into BI
    cmd_joinoutput = ( "SELECT a.ID,a.Division,a.Language,a.Create_Date,a.Event_Date,a.Training_program,a.Trainer_name,a.Last_Name," \
                       "a.Name,a.Company,a.mail,a.Role,a.Cellphone,a.Telephone,a.Comments,a.Comments_1,a.Comments_2,a.global_satisfaction," \
                       "a.nps_eu,a.nps,b.* FROM survey a LEFT JOIN questions b ON a.ID=b.ID " \
                       "WHERE a.Create_Date IS NOT '' AND a.ID <> '%s'" % i)

    #print(type(infolist))
    for temp in infolist:
        cursorlite.execute(cmd_insert_survey,(i,Division ,lang, temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7],
                            temp[8], temp[9], temp[10],temp[21], temp[27],
                            temp[33], temp[34], 'NA', 'NA'))


        cursorlite.execute(cmd_insert_questions, (i, "Q1", temp[11]))
        cursorlite.execute(cmd_insert_questions, (i, "Q2", temp[12]))
        cursorlite.execute(cmd_insert_questions, (i, "Q3", temp[13]))
        cursorlite.execute(cmd_insert_questions, (i, "Q4", temp[14]))
        cursorlite.execute(cmd_insert_questions, (i, "Q5", temp[15]))
        cursorlite.execute(cmd_insert_questions, (i, "Q6", temp[16]))
        cursorlite.execute(cmd_insert_questions, (i, "Q7", temp[17]))
        cursorlite.execute(cmd_insert_questions, (i, "Q8", temp[18]))
        cursorlite.execute(cmd_insert_questions, (i, "Q9", temp[19]))
        cursorlite.execute(cmd_insert_questions, (i, "Q10", temp[20]))
        cursorlite.execute(cmd_insert_questions, (i, "Q11", temp[22]))
        cursorlite.execute(cmd_insert_questions, (i, "Q12", temp[23]))
        cursorlite.execute(cmd_insert_questions, (i, "Q13", temp[24]))
        cursorlite.execute(cmd_insert_questions, (i, "Q14", temp[25]))
        cursorlite.execute(cmd_insert_questions, (i, "Q15", temp[26]))
        cursorlite.execute(cmd_insert_questions, (i, "Q16", temp[28]))
        cursorlite.execute(cmd_insert_questions, (i, "Q17", temp[29]))
        cursorlite.execute(cmd_insert_questions, (i, "Q18", temp[30]))
        cursorlite.execute(cmd_insert_questions, (i, "Q19", temp[31]))
        cursorlite.execute(cmd_insert_questions, (i, "Q20", temp[32]))
        #cursorlite.commit()

        i += 1

##Validation
    '''
    cursorlite.execute(cmd_select_survey)
    result2 = cursorlite.fetchall()

    cursorlite.execute(cmd_select_questions)
    result1 = cursorlite.fetchall()

    for line in result2:
       print(line)

    for line in result1:
       print(line)

    cursorlite.execute(cmd_joinoutput)
    output = cursorlite.fetchall()
    for line in output:
        print(line)
'''
## Insert into BI Database

    cursor.execute(cmd_prod_cleaning_staging)
    cursorlite.execute(cmd_joinoutput)
    result = cursorlite.fetchall()
    for line in result:
        cursor.execute(cmd_prod_insert, (line[0],line[1],line[2],line[3],
                                        line[4],line[5],line[6],line[7],
                                        line[8],line[9],line[10],line[11],
                                        line[12],line[13],line[14],line[15],
                                        line[16],line[21],line[22],line[17],line[18],line[19]
                                        ,now))
        #cursor.commit()

    cursor.execute(cmd_prod_executesp,lang)

## Close connections
    closecursor(cursor)
    closecursor(cursorlite)



def googlemanipulationformation(division,sp,info):
    ## connection parameters
    cursor = odbconnection()

    ## SQL Queries library
    cmd_cleanstaging = 'TRUNCATE TABLE T_SAS_Staging_Formation'
    cmd_insertstaging = 'INSERT INTO T_SAS_Staging_Formation VALUES ' \
                        '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,' \
                        ' ?,?,?,?,?,?,?,?,?,?,?)'

    cmd_spmovedata = "EXEC %s" % sp

    ##Execution queries and load data in BI
    cursor.execute(cmd_cleanstaging)
    for row in info:

        cursor.execute(cmd_insertstaging,(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],
                                          row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[24], row[27],
                                          row[28], row[29], row[30], row[31], row[32], row[33], row[34],''))


    cursor.execute(cmd_spmovedata)

    ## Close connections
    closecursor(cursor)
