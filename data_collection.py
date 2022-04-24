'''
 # @ Author: Veenay
 # @ Create Time: 2021-08-20 11:29:22
 # @ Modified by: Veenay
 # @ Modified time: 2021-08-20 15:59:27
 '''
# -*- coding: utf-8 -*-

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/ds_salary_estimator/data_collection/scraping-glassdoor-selenium/chromedriver"

df = gs.get_jobs('data analyst',500, False, path, 15)
df.to_csv('glassdoor_data_analyst_jobs.csv', index = False)


