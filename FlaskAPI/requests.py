'''
 # @ Author: Veenay
 # @ Create Time: 2021-08-20 11:29:24
 # @ Modified by: Veenay
 # @ Modified time: 2021-08-20 16:01:26
 '''


import requests
from data_input import data_in

URL = ' http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}


if __name__ == '__main__':
    r = requests.get(URL,headers=headers,json=data)
    print(r.json())