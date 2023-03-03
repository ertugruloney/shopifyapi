#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 00:03:26 2022

@author: ertugruloney
"""

import mysql.connector as mysql
import pandas as pd
import requests

API_KEY ='83b7930370183629c4e7905332daae2e'
PASSWORD = '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'
SHOP_NAME = 'xoxsosft2'

def updateprod(API_KEY,PASSWORD,SHOP_NAME):
    url = "https://%s:%s@%s.myshopify.com/admin/api/2022-10/products/%s.json" % (API_KEY, PASSWORD, SHOP_NAME,8035878502688)
    payload = {
      "product": {
       
        "variants": [
            
   {
	

  "inventory_quantity":0 

    
        }]
     }
    }
    
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    r = requests.put(url, json=payload,  headers=headers)
    print("stok güncellemesi yapıldı")
updateprod(API_KEY,PASSWORD,SHOP_NAME)


def get_count(API_KEY,PASSWORD,SHOP_NAME):
    url = "https://%s:%s@%s.myshopify.com//admin/api/2022-10/products/count.json" % (API_KEY, PASSWORD, SHOP_NAME)
    r=requests.get(url)
    return r.json()
def get_det(API_KEY,PASSWORD,SHOP_NAME):
    url = "https://%s:%s@%s.myshopify.com//admin/api/2022-10/products.json" % (API_KEY, PASSWORD, SHOP_NAME)
    r=requests.delete(url)
    return r.json()
countt=get_count(API_KEY,PASSWORD,SHOP_NAME)
