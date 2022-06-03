#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:58:48 2022

@author: samkd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pyp
import sqlite3 as sql

def startdb():
    global connection, cursor
    connection = sql.connect('cop503cw.db')
    cursor = connection.cursor()
# close database
def closedb():
    connection.commit()
    connection.close()
    

def read_tables(table):
    """
    this is a function for if you want to read one table from the student database.
    table = the table from the sql database. 
    """
    connection = sql.connect('cop503cw.db')
    x = pd.read_sql(table,connection)
    return x

def grab_tables(listofdata,emptylist):
    """
    will read tables from student database at once into a list named dataframes. 
    returns dataframes as dfs.
    listofdata = a list of files you want to be read into dataframes.
    emptylist = requires an empty list to store the dataframes into.
    """
    for item in listofdata:
        emptylist.append(read_tables(item))
    print("Data has now been read")
    return emptylist
    connection.close()
    
def combine_all_data(dfs,by):
    """
    will join all datframes together after you use grab_tables function
    returns all_student_data
    dfs = requires dataframe list 
    by = what you want to join the tables by
    """
    all_student_data=pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(dfs[0],dfs[1],on= by),dfs[2],on= by), dfs[3], on=by), dfs[4], on = by),dfs[5], on = by)
    all_student_data = all_student_data.set_index("researchid")
    indexes = list(all_student_data.filter(regex='index'))
    all_student_data = all_student_data.drop(indexes, axis=1)
    all_student_data.columns = ["Startedon1","Completed1","Grade1","Q1t1","Q2t1","Q3t1","Q4t1","Q5t1","Q6t1","Startedon2",
                     "Completed2","Grade2","Q1t2","Q2t2","Q3t2","Q4t2","Q5t2","Q6t2","Startedon3","Completed3","Grade3",
                     "Q1t3","Q2t3","Q3t3","Q4t3","Q5t3","Q6t3","Startedon4","Completed4","Grade4","Q1t4","Q2t4",
                     'Startedon_m','Completed_m','Grade_m','Q1_m','Q2_m','Q3_m','Q4_m','Q5_m','Q6_m','Q7_m','Q8_m',
                     'Q9_m','Q10_m','Startedon_s','Completed_s','Grade_s','Q1_s','Q2_s','Q3_s','Q4_s','Q5_s','Q6_s', 
                     'Q7_s', 'Q8_s','Q9_s','Q10_s','Q11_s', 'Q12_s','Q13_s']
    return all_student_data

def read_survey():
    """
    survey takes filepath of survey and reads it into system, 
    needed for hardworking_students function

    Returns
    -------
    survey : TYPE
        DESCRIPTION.

    """
    surveypath = input("enter survey file path:")
    survey = surveypath
    survey = pd.read_csv(survey)
    survey.columns = survey.columns.str.replace(" ","")
    survey = survey.set_index("researchid")
    return survey

