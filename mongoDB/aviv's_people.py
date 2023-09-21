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
army_data.delete_one({"name": "Lihi"})

query_1 = {
    "age": {"$lt": 23},  
    "role": "DevOps"  
}
result1 = army_data.find_one(query_1)
if result1:
    print(f"Name of the person: {result1['name']}")
else:
    print("No person matching the criteria found.")

same_age_person = army_data.find_one({"age": result1["age"], "_id": {"$ne": result1["_id"]}})
if same_age_person:
    new_role = same_age_person["role"]
    army_data.update_one(
        {"_id": result1["_id"]},
        {"$set": {"role": new_role}}
    )
    print(f"Replaced {result1['name']}'s role with {same_age_person['name']}'s role.")
else:
    print("No person of the same age found.")


query_older_than_23 = {"age": {"$gt": 23}}
older_people = list(army_data.find(query_older_than_23).sort("age", -1))


for person in older_people:
    if person["age"] > 23:
        friends_data.insert_one(person)

for person in older_people:
    print(f"Name: {person['name']}, Age: {person['age']}, role: {person['role']}")

for person in army_data.find({"age": {"$lte": 23}}).sort("age"):
    print(f"Name: {person['name']}, Age: {person['age']}, role: {person['role']}")









