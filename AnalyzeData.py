from pymongo import MongoClient
from sklearn import tree
import GatheringData
import math

cityName = input("Ort: ") or " "
if " " in cityName:
    cityName.replace(" ","-")
cityName = cityName.lower()
GatheringData.cityName = cityName
GatheringData.houseFinder(cityName)

input_area = input("Wohnfläche: ") or 0
input_area = int(input_area)
input_rooms = input("Zimmer: ") or 0
input_rooms = int(input_rooms)
client = MongoClient("mongodb://127.0.0.1:27017")
mdb = client["Immowelt"]
mcol = mdb["Wohnungen"]
area_rooms = []
price = []

# Query to find car in database
count = 0
print(f"Stadt: {cityName}")
for x in mcol.find({},{ "_id": 0}):
    area = float(x["area"])
    rooms = float(x["rooms"])
    # Check if the float number is close to the integer
    if math.isclose(area,input_area,abs_tol=0.9) and \
       math.isclose(rooms,input_rooms,abs_tol=0.9) and cityName == x["city"]:
        count+=1 
        print(f"Wohnung #{count}\n Die Größe: {area}\n Zimmer: {rooms}\n Price: {x['price']}\n Link: {x['link']}")
        print("----------------") 
    elif input_area != area and input_rooms != rooms and cityName == x["city"]:
        area_rooms.append([area,rooms])
        price.append(x["price"])
if count == 0:
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(area_rooms,price)
    new_data = [[input_area,input_rooms]]
    answer = clf.predict(new_data)
    print(f"Keine Wohnung habe ich im Moment gefunden aber \neine Wohnung mit {input_rooms} Zimmer und Größe {input_area} kostet etwa {answer[0]} Euro pro Monat!")


client.close()
