import pymongo
from bson import ObjectId
cilent = pymongo.MongoClient('mongodb://admin:admin@ds021182.mlab.com:21182/c4e', retryWrites = False)
db = cilent['c4e']
posts_collection = db['posts']

#Exercise3
posts_collection.insert_one({
    "title": "Vội vàng",
    "author": "Xuân Diệu",
    "content": "...Xuân đương tới, nghĩa là xuân đương qua,\nXuân còn non, nghĩa là xuân sẽ già,..."
})

#Exercise4
from matplotlib import pyplot
customers_collection = db['customers']

ref_counts = []
ref_names = []
result = customers_collection.aggregate([
    { "$group": {"_id": "$ref", "count":{"$sum":1}}}
]) 
for x in result:
    print(x)
    ref_counts.append(x["count"])
    ref_names.append(x["_id"])
pyplot.pie(ref_counts, labels = ref_names, autopct = "%.1f%%", shadow = True, explode = [0,0,0.1])
pyplot.title('Customers grouped by refs')
pyplot.axis('equal')

pyplot.show()
