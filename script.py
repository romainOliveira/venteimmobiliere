from pymongo import MongoClient
import requests
from re import search
from ipywidgets import interact

client = MongoClient("") 

db = client.projet
collection_estate = db['estate']

cur = collection_estate.aggregate([
    {'$group':{'_id':'$id','price': {"$sum": "$price"},'département': "$dpt"}},
    {"$sort":{"price": -1}},
    { "$limit" : 10 }
])
list(cur)

cur = collection_estate.aggregate([
    {"$group": {"_id": {},"price": {"$avg": "$price"}}},
    {"$limit": 5000}
])
list(cur)

def f(dpt):  
    cur = collection_estate.aggregate([
        {"$match": {"dpt": dpt}},
        {"$unwind": "$price"},
        {'$group':{'_id':'$id','price': {"$sum": "$price"},'département': "$dpt"}},
    ])

def get_highest_price(self):
        cur_highest_price = self.collection_estate.find({'Type': 'Venta'}).sort('Price', -1).limit(5)
        return cur_highest_price