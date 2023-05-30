# from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current

# client = MongoClient('mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23')
# result = client['interns_b2_23']['Chinmoy'].aggregate([
#     {
#         '$group': {
#             '_id': 0, 
#             'total': {
#                 '$sum': '$price'
#             }
#         }
#     }, {
#         '$project': {
#             '_id': 0
#         }
#     }
# ])

agg_code = [
    {
        '$group': {
            '_id': 0, 
            'total': {
                '$sum': '$price'
            }
        }
    }, {
        '$project': {
            '_id': 0
        }
    }
]