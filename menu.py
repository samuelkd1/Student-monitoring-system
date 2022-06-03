#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 02:27:21 2022

@author: samkd
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyp
import sqlite3 as sql
from DAFunction import *
from testResults import *
import matplotlib.pyplot as pyp
from studentPerformance import *
from underperformingStudent import *
from hardworkingStudents import *

def menu():
    """
    A menu that does certain commands depending on the number chosen. 
    For almost all of the actions the data needs to be read and all test data 
    needs to be retrieved.

    Returns
    -------
    None.

    """
    ans = True
    while ans:
        print(""" 1. GRAB STUDENT DATABASE
               \n 2. GET ALL TEST DATA 
               \n 3. GET STUDENT TEST RESULTS 
               \n 4. GET STUDENT OVERVIEW ON PERFORMANCE
               \n 5. SHOW UNDERPERFORMERS
               \n 6. SHOW HARDWORKING STUDENTS""")
        ans = input("PLEASE SELECT AN OPTION (7 TO EXIT): ") 
        if ans == "1":
            startdb()
            print("\n Student Database on system")
        elif ans == "2":
            sql_test_1 = """ SELECT * FROM rtest_1 """
            sql_test_2 = """SELECT * FROM rtest_2 """
            sql_test_3 = """SELECT * FROM rtest_3"""
            sql_test_4 = """SELECT * FROM rtest_4"""
            sql_mock = """ SELECT * FROM rmock_test """
            sql_sum = """SELECT * FROM rsum_test """
            sqltables = [sql_test_1, sql_test_2, sql_test_3, sql_test_4, sql_mock, sql_sum]
            dfs = []
            grab_tables(sqltables,dfs)
            data = combine_all_data(dfs,by = "researchid")
            print("\n All STUDENT DATA")
            print(data)
        elif ans == "3":
            try:
                grab_test_marks(data)
            except NameError:
                print("\n YOU NEED TO SELECT OPTION 1 AND 2 FIRST\n")
        elif ans == "4":
            try:
                test = int(input("Enter test(5 for mock test, 6 for summative):"))-1
                student_id = int(input("Enter student ID:"))
                print("Student %s results"%(student_id))
                student_perf(test, student_id,dfs)
            except NameError:
                print("\n SELECT OPTION 1 AND 2 FIRST\n")
        elif ans == "5":
            try:
                print("Students that need support")
                underperforming_students(data)
            except NameError:
                print("\n SELECT OPTION 1 AND 2 FIRST\n")
        elif ans == "6":
            try:
                survey = read_survey()
                print("Hardworking students that deserve praise")
                hardworking_students(survey, data)
            except:
                print("\n SELECT OPTION 1 AND 2 FIRST\n")
        elif ans == "7" :
            print("\n Goodbye") 
            ans = None
        else:
            print("\n NOT A VALID ANSWER TRY AGAIN")
        