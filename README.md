# Data Science Data Analyst Salary Estimator
# Project Overview 
* Created a tool that estimates data science salaries (MAE) to help data analysts negotiate their income when they get a job.
* Scraped over 500 job descriptions from glassdoor Malaysia using python and selenium
* Engineered features from the text job description to get insight of companies put on power bi, tableau, python, sql,excel and machine_learning. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

## Code and Resources Used 
**Python Version:** 3.9  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium  
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Web Scraping
In the project, web scraper github repo (above github link) was used to scrape 500 job postings from Malaysia glassdoor website. With each job, we got the following:
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

## Data Cleaning
After the data has been scrapped, I need to clean it up before using in the models. I cleaned and changed variables as follows:

*	Parsing salary data
*	Drop rows without salary 
*	Made columns for hourly wages  
*	Convert company founded date into age of company 
*   Parsing job description
*   Extract relevant skills from the job description and make separate columns for each of it:
    * Power BI  
    * Tableau  
    * Python  
    * SQL  
    * Excel 
    * Machine Learning
*	Create column for simplified job title
*	Create column for job description length 

## Exploratory Data Analysis
I looked in the distributions of the data and categorical variables using pivot tables and other visualization. Below are a few pictures:

![job_numbers_vs_location](https://user-images.githubusercontent.com/72549846/130232033-0a0d2975-73b4-4d5f-8aff-03b843a8bde0.PNG "Job numbers vs Location")
![job_numbers_vs_job_title](https://user-images.githubusercontent.com/72549846/130231975-cad78558-a547-453e-a6df-00476610a840.PNG "Job numbers vs Job title")
![correlation](https://user-images.githubusercontent.com/72549846/130231915-da92536c-b6f2-4e53-b892-8eb0a17a4acf.PNG "Correlations")

## Model Building 
Transformed categorical variables into dummy variables. Then I split the data into train and tests sets with test size of 20% and 80% for train set respectively.  

I implement three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest Regressor** – Again with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Linear Regression** : Negative MAE = -5.15
*	**Lasso Regression**: Negative MAE = -12.68 and -4.88(after tuned)
*	**Random Forest**: Negative MAE = -2.52
*	**GridSearchCV(Random Forest)**: Negative MAE = -2.12
## Productionization 
For this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary. 
