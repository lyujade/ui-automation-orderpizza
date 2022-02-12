import requests
import json
import random
url="http://localhost:3001/api/order"
rq=requests.get(url)
print(rq.status_code)
print(rq.text)
rt=json.loads(rq.text)
# print(rt["orderId"])
orderId=rt["orderId"]

size=["small","medium","large"]

size=random.choices(size)
print(size)
# toppings=[["cheese"],["bacon"],["egg"]]

data1={"pizzas": [{"size": size, "toppings": ["cheese"]},{"size": size, "toppings": ["bacon","egg"]},{"size": size, "toppings": ["bacon","egg"]}],"orderId":orderId}
rt2=requests.post(url,json=data1)
#
print(rt2.text)
text=json.loads(rt2.text)

print(text["success"]==True)
print(rt2.status_code)
