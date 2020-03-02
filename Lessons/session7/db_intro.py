#Cilent/Database/Collections/Records
#trước tiên phải vào cmd type mongod ~ chạy mongodb.exe
import pymongo
from bson import ObjectId

#CREATE
cilent = pymongo.MongoClient('mongodb://localhost:27017/')
db = cilent['c4e']
customer_collection = db['customer']

# new_data = [
#     {'name': 'không phải học viên',
#     'age': '15',
#     'address': '22c thành công'
#     },
#     {'name': 'không phải học viên',
#     'age': '16',
#     'address': '23c thành công'
#     },
#     {'name': 'không phải học viên',
#     'age': '17',
#     'address': '24c thành công'
#     },
# ]
# customer_collection.insert_many(new_data)
# # # insert_one({
# # #     'name': 'không phải học viên',
# # #     'age': '15',
# # #     'address': '22c thành công'
# # })

# #READ
# # data = customer_collection.find({})
# # data = customer_collection.find({'name': 'Min'}) #{} tim du lieu kieu object; kieu du lieu cua _id là OblectId cua rieng Mongo; ":" tim chinh xac gia tri; 
# # data = customer_collection.find_one({'age': {'$lt': '18'}}) #$ danh dau bieu thuc so sanh cua Mongo, lt: less than; tuổi để dạng chữ nhưng Mongo vẫn so sánh được nhưng Python thì lỗi; find({...}) tìm nhiều, find_one: tìm cái đầu tiên theo cách sắp xếp mặc định, thường tìm theo _id để tránh trùng lặp

# data = customer_collection.find_one({'_id': ObjectId('5e551dea35a568b09a8ed955')})
# print(data)
# #print(data['name])
# # for customer in data: #khong phai list nhung 1 so cho co the lam nhu list
# #     print(customer) 

# #UPDATE
# customer_collection.update_one(
#     {
#         '_id': ObjectId('5e551dea35a568b09a8ed955')
#     },
#     {
#         '$set':{
#             'name': 'Không phải Phượngx'
#         }
#          # không có $set ghi đè tất cả dữ liệu của các key -> Mongo không cho chạy
#          # => chỉ sửa 1 key
#     }
# )

#DELETE
# customer_collection.delete_one({'_id': ObjectId('5e551dea35a568b09a8ed955')})

from faker import Faker
fake = Faker()
new_data= []
for i in range(100):
    customer = {
        'name': fake.name(),
        'phone_number': fake.phone_number(),
        'address': fake.address()
    }
    new_data.append(customer)

customer_collection.insert_many(new_data)
#insert_one({'name':'new_data'})

