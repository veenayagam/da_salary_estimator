# Data Analyst Salary Estimator
# Project Overview 
* Create a tool that estimates data analyst salaries based on (MAE) to help data analysts negotiate their income when they get a job.
* Scraped over 500 job descriptions from Glassdoor Malaysia using python and selenium
* Engineered features from the text job description to get an insight of companies put on power bi, tableau, python, sql,excel and machine_learning. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client-facing API using flask 

## Code and Resources Used 
**Python Version:** 3.9  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium  
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping
In the project, the web scraper GitHub repo (above Github link) was used to scrape 500 job postings from Malaysia glassdoor website. With each job, below are the following features:
*	Job title
*	Rating
*	Location
*	Company Size
*	Type of ownership 
*	Industry
*	Sector
*	Revenue
*	Company Founded Date
*	Job description

## Feature Engineering
After the data has been scrapped, it needs to clean up before using in the models. The data went cleaning and changing variables as follows:

*	Parsing salary data
*	Drop rows without salary 
*	Made columns for hourly wages  
*	Convert company founded date into age of company 
*   Parsing job description
*   Extract relevant skills from the job description and make separate columns for each of them:
    * Power BI  
    * Tableau  
    * Python  
    * SQL  
    * Excel 
    * Machine Learning
*	Create a column for simplified job title
*	Create a column for job description length 

There were some studies been performed by analyzing the distributions of the data and categorical variables using pivot tables and other visualization. Below are a few pictures:

![job_numbers_vs_location](https://user-images.githubusercontent.com/72549846/136419596-c3158210-54bd-43f8-8ce7-748d133f0070.png "Job numbers vs Location")
![job_numbers_vs_job_title](https://user-images.githubusercontent.com/72549846/136419615-1b4d31ed-ff56-4077-a3fd-ace6ee310e4e.png "Job numbers vs Job title")

## Model Building 
The features have been transformed into categorical variables into dummy variables. Then it undergoes splitting the data into train and tests sets with a test size of 20% and 80% for a train set respectively. 

There were three different models were implemented and evaluated them using Mean Absolute Error. MAE is preferable because it is relatively easy to interpret and outliers aren???t particularly bad in??this type of model.

Below are the three different models:
*	**Multiple Linear Regression** ??? Used as a baseline for the model.
*	**Lasso Regression** ??? Used because normalized regression like lasso would be effective for sparse data from the many categorical variables.
*	**Random Forest Regressor** ??? Used because again with the sparsity associated with the data, this model would be a good fit. 

## Model Performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Linear Regression** : Negative MAE = -5.15
*	**Lasso Regression**: Negative MAE = -12.68 and -4.88(after tuned)
*	**Random Forest**: Negative MAE = -2.52
*	**GridSearchCV(Random Forest)**: Negative MAE = -2.12
## Model Deployment
For this step, flask API endpoint that was hosted on a local web server has been built by following along with the tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.??
