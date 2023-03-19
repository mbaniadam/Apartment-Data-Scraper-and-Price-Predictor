from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient , ASCENDING
import re
from sklearn import tree

def houseFinder(cityName):
    r = requests.get(f'https://www.immowelt.de/liste/{cityName}/wohnungen/')
    soup = BeautifulSoup(r.text,"html.parser")
    WDE = soup.find_all("div", class_=re.compile("EstateItem.*"))
    #print("*** Wohnung mieten im Deutschland ***")
    client = MongoClient("mongodb://127.0.0.1:27017")
    mdb = client["Immowelt"]
    mcol = mdb["Wohnungen"]
    mcol.create_index([("link", ASCENDING)], unique=True)
    #mcol.drop()
    # Find and insert into database
    insertError = False
    for item in WDE:
        area = item.find("div", attrs={"data-test":"area"}).contents[0]
        area = float(area.split(" ")[0])
        rooms = item.find("div", attrs={"data-test":"rooms"}).contents[0]
        rooms = rooms.split(" ")[0]
        price = item.find("div", attrs={"data-test":"price"}).contents[0]
        price = price.split(" ")[0]
        link = item.find("a", href=True)["href"] 
        #print(area,price)
        data = {"city":cityName,"area":area,"rooms":rooms,"price":price,"link":link}
        try:
            mcol.insert_one(data)
        except Exception:
            insertError = True

    if insertError:
        print("Error occurred while inserting data")

    client.close()

cityName = ""
#houseFinder(cityName)