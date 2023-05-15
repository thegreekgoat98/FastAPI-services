from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

client = MongoClient('mongodb://localhost:27017/')
result = client['Books']['chinmoy'].aggregate([
    {
        '$group': {
            '_id': 0,
            'total': {
                '$sum': '$book_price'
            }
        }
    }
])

# Aggregate pipeline for getting sum of all books
