import mysql.connector as mysql
import pandas as pd
import requests

from base64 import b64encode
API_KEY =''
PASSWORD = ''
SHOP_NAME = ''
url = "https://%s:%s@%s.myshopify.com/admin/api/2022-10/products.json" % (API_KEY, PASSWORD, SHOP_NAME)
path="/Users/ertugruloney/Desktop/bionluk işler/shoifyapi/saat.jpg"

with open(path, "rb") as f:
    code=b64encode(f.read())
    b=code.decode('utf-8')
mydb = mysql.connect(
  host="localhost",
  database='Shopify',
  user="root",
  password="",
  )
mycursor = mydb.cursor()

sql = "SELECT * From Sheet3 "

mycursor.execute(sql)

myresult = mycursor.fetchall()
myresult=list(myresult)
myresult=myresult[0:2]
kayitlar=pd.read_excel("sonkayit.xlsx")
def imageyukleme(data,API_KEY,PASSWORD,SHOP_NAME):
    url = "https://%s:%s@%s.myshopify.com/admin/api/2022-10/products/%s/images.json" % (API_KEY, PASSWORD, SHOP_NAME,data[1])
    payload = {
        
    "image": {
    "id": 1001473896,
    "product_id": data[1],
    
    "image.file":"/Users/ertugruloney/Desktop/bionluk işler/shoifyapi/saat.jpg"
    
   
  }


     }
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    r = requests.put(url, json=payload,  headers=headers)
    
def get_producT(url):
    r=requests.get(url)
    return r.json()

def creat_product(url,data,b):

      payload = {
        "product": {
        "id":data[1],
          "title": data[2],
          "images": [{  
                      "attachment":b}],

          "variants": [
              
     {
  	"product_id": data[1],   
    "price":int(data[6]),
    "barcode":data[10],
  	"compare_at_price":int(data[4]),
    "inventory_quantity":int(data[9][:-4]),
    "inventory_management": "shopify",
    "inventory_policy": "continue",
      
          }]
       }
      }

      headers = {"Accept": "application/json", "Content-Type": "application/json"}

      r = requests.post(url, json=payload,  headers=headers)
    
def updateprod(data,API_KEY,PASSWORD,SHOP_NAME):
    url = "https://%s:%s@%s.myshopify.com/admin/api/2022-10/products/%s.json" % (API_KEY, PASSWORD, SHOP_NAME,data[1])
    payload = {
      "product": {

        "variants": [
            
   {
	

  "inventory_quantity":int(data[9][:-4]),

    
        }]
     }
    }
    
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    r = requests.put(url, json=payload,  headers=headers)
    print("stok güncellemesi yapıldı")
prod=get_producT(url)
if len(kayitlar)==0:
    kayitlar=[]
    for i in myresult:
        

        i=list(i)
        price=i[6][:-3]
        price=price.replace(".","")
        i[6]=price
        cprice=i[4][:-3]
        price=price.replace(".","")
        i[4]=price
        creat_product(url,i,b)
        imageyukleme(i,API_KEY,PASSWORD,SHOP_NAME)
        idd=i[1]
        kayitlar.append([idd,i[9]])
    kayitlar=pd.DataFrame(kayitlar)
    #kayitlar.to_excel("sonkayit.xlsx")
else:
    kayitlar=kayitlar.iloc[:,1:3].values.tolist()
    for j in myresult:
        durum=0#kayıt varmı
      
        for count,i in enumerate( kayitlar):
            
       
            if i[0]==j[1]:
                durum=1
                if i[1]!=j[9]:
                    updateprod(j,API_KEY,PASSWORD,SHOP_NAME)
                    kayitlar[count][1]=j[9]
                break
        if durum==0:
            
            i=list(j)
            price=i[6][:-3]
            price=price.replace(".","")
            i[6]=price
            cprice=i[4][:-3]
            price=price.replace(".","")
            i[4]=price
            creat_product(url,i)
            idd=i[1]
            kayitlar.append([idd,i[9]])
            
kayitlar=pd.DataFrame(kayitlar)
#kayitlar.to_excel("sonkayit.xlsx")