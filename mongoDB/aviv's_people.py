from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["Aviv's_people"]
family_data = db["family"]
friends_data = db["friends"]
army_data = db["army"]

friends = [
    {"name": "Amit", "age": 20, "role": "waiter"},
    {"name": "Yoav", "age": 24, "role": "doctor"},
    {"name": "Noa", "age": 22, "role": "student"},
    {"name": "Michal", "age": 21, "role": "baker"}   
]

for person in friends:
    friends_data.insert_one(person)

family = [
    {"name": "mother", "age": 45, "role": "teacher"},
    {"name": "father", "age": 46, "role": "engineer"},
    {"name": "brother", "age": 12, "role": "school"},
    {"name": "sister", "age": 24, "role": "student"}
    
]
family_data.insert_many(family)

army = [
    { "_id": 10, "name": "Aviv", "age": 20, "role": "backend"},
    { "_id": 20,"name": "Lihi", "age": 21, "role": "OA"},
    { "_id": 30,"name": "Gabi", "age": 22, "role": "DevOps"},
    { "_id": 40,"name": "ori", "age": 23, "role": "Front-end"},
     { "_id": 50,"name": "ido", "age": 22, "role": "Developer"},
    { "_id": 60,"name": "yarden", "age": 24, "role": "DevOps"}
]

#army_data.insert_many(army)
army_data.delete_one({"name": "Lihi"})

