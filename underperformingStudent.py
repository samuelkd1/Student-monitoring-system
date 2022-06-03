#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:25:50 2022

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


def underperforming_students(all_tests):
    """
    Will print and return all underperfoming students.
    students are considered underperforming when they have achievied a mark 
    below ten percent of the mean summative grade.
    excludes disengaged students in this case are any students that got a 0 in 
    the formative tests.
    from lowest grade to highest

    Parameters
    ----------
    all_tests : dataframe 
        dataframe containing marks on all questions and their total grade.

    Returns
    -------
    underperforming_students : dataframe
        returns all the grades and ids of underperforming students and also shows
        their worst performing summative test.

    """
    try:
        avg_summative_grade = all_tests.Grade_s.mean() 
        underperforming_benchmark = avg_summative_grade*0.9 # to find 10% 
        underperforming_students = all_tests[all_tests["Grade_s"] < underperforming_benchmark]
        underperforming_students = underperforming_students.filter(regex='Grade')
        underperforming_students = underperforming_students.sort_values("Grade_s")
        columns=['Grade1','Grade2',"Grade3","Grade4"] # ensuring it only does formative tests
        underperforming_students = underperforming_students.replace(0, np.nan).dropna(axis=0, how='any', subset=columns).fillna(0).astype(int)
        highlights = ['Grade1','Grade2',"Grade3","Grade4","Grade_m"]
        underperforming_students["Lowest_mark"] = underperforming_students[highlights].idxmin(1)
        print(underperforming_students)
        return underperforming_students
    except IndexError:
        print("Test not found")



