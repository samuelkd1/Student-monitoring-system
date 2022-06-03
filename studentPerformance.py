#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 04:55:51 2022

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


def student_perf(test, student,dfs):
    """
    Will get the absolute and relative performance of a student 
    then plot it as multiple grapths to show a students performance for the test chosen

    Parameters
    ----------
    test : picking a test 5 is the formative mock test and 6 is the summative test.
    student : student_id
        DESCRIPTION.
    dfs : dataframe of tests.

    Returns
    -------
    student : dataframe on the performance of the student for that particular test.

    """
    if test >= 0 and student > 0:
        test = dfs[test].set_index("researchid")
        test = test.drop("index", axis=1)
        test = test.rename(columns = {"Grade": "Absolute_performance"})
        mean = test.Absolute_performance.mean()
        test["relative_performance"] = test[["Absolute_performance"]]-mean
        student = test.loc[[student]]
        print (student)
        questions_plot = student.filter(regex ='Q')
        absolute_and_rel = student.filter(regex ='performance')
        questions_plot.T.plot(title = "Performance on each question")
        student.plot(kind = "bar")
        absolute_and_rel.plot(kind = "bar")
        pyp.show()
        return student
    else:
        print("Try again")