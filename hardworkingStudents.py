#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 02:05:47 2022

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

def hardworking_students(survey, all_tests):
    """
    Will print hardworking students from highest summative grade that achieved over 60
    and also those that responded "below beginner" or "beginner" in the survey

    Parameters
    ----------
    survey : dataframe
        survey of the students needed.
    all_tests : dataframe
        all tests, obtained from earlier functtion.

    Returns
    -------
    hardworking_students : dataframe
        has all ids of hardworking students.

    """
    all_tests = all_tests[["Grade_s"]]
    student_rates = survey[["Whatlevelprogrammingknowledgedoyouhave?"]]
    student_rates = student_rates.rename(columns = {"Whatlevelprogrammingknowledgedoyouhave?": "programming_lvl"})
    student_rates = pd.merge( all_tests, student_rates ,on= "researchid")
    hardworking_students = student_rates[(student_rates["Grade_s"]> 60) 
                                     & (student_rates["programming_lvl"]== "Below beginner")|
                                     (student_rates["programming_lvl"]== "Beginner")]
    hardworking_students = hardworking_students.sort_values("Grade_s", ascending = False)
    print(hardworking_students)
    return hardworking_students