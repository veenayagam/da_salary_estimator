# -*- coding: utf-8 -*-
'''
Created Date: Saturday August 14th 2021
Author: <<Veenay>>
'''

import glassdoor_scraper as gs 
import pandas as pd 

path = "C:/Veenayagam_Things/ML-things/ML Projects/ds_salary_estimator/data_collection/scraping-glassdoor-selenium/chromedriver"

df = gs.get_jobs('data analyst',500, False, path, 15)
df.to_csv('glassdoor_data_analyst_jobs.csv', index = False)


