import pymongo
from bson import ObjectId
from faker import Faker
faker = Faker()

cilent = pymongo.MongoClient('mongodb://localhost:27017/')
db = cilent['c4e']
customer_collection = db['customer']

new_data = []
for i in range(100):
    data = {
        'name': faker.name(),
        'address': faker.address(),
        'phone': faker.phone_number()
    }
    new_data.append(data)

customer_collection.insert_many(new_data)