#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 19:27:10 2022

@author: samkd
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyp
import sqlite3 as sql

def grab_test_marks(all_student_data):
    """
    Function to obtain the test marks of students inputted 
    
    Parameters
    ----------
    all_student_data : datafrane
        all of the tests and question marks for the students.

    Returns
    -------
    grades : dataframe
        will return the grades of the inputted student id.

    """
    all_student_data = all_student_data.filter(regex='Grade').astype(int)
    all_student_data = all_student_data.reindex(index=all_student_data.index[::-1])
    all_student_data.columns = ["test_1","test_2","test_3","test_4","mock_test","summative_test"]
    student_id = int(input("Please enter ID to see grades:"))
    try:
        if student_id > 0:
            grades=all_student_data.loc[[student_id]]
            print(all_student_data.loc[[student_id]])
            grades.T.plot(kind="bar", title = "Student Grades", ylabel = "Percentage (%)")
            pyp.show()
            return grades
        else:
            print("Student not found try again")
    except KeyError:
        print("Student not found try again")
       