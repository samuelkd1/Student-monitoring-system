#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 03:21:56 2022

@author: samkd
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as pyp
import sqlite3 as sql

connection = sql.connect('cop503cw.db')
cursor = connection.cursor()

sql_test_1 = """ SELECT * FROM rtest_1 """
sql_test_2 = """SELECT * FROM rtest_2 """
sql_test_3 = """SELECT * FROM rtest_3"""
sql_test_4 = """SELECT * FROM rtest_4"""
sql_mock = """ SELECT * FROM rmock_test """
sql_sum = """SELECT * FROM rsum_test """

