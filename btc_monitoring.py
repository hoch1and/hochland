#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import time 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import warnings
warnings.filterwarnings('ignore')


# In[ ]:


def request(URL):
    response = requests.get(URL)
    response_json = response.json()
    return float(response_json["USD"]["last"])


URL = 'https://blockchain.info/ru/ticker'
temp = 0
while True:
    current_time = time.strftime("%H:%M:%S", time.localtime())
    price = request(URL)
    if price != temp:
        print('-' * 18)
        print(f'Время: {current_time}\nЦена BTC: {price}')
        temp = price

