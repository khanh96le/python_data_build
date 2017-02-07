import pymongo
from pymongo import MongoClient
import requests, json

from pandas import DataFrame

client = MongoClient()

db = client.test_database

collection = db.test_collection

apples = client.db.apples

url = "https://en.wikipedia.org/w/api.php?action=opensearch&search=apple&limit=10&namespace=0&format=json"
data = json.loads(requests.get(url).text)

df = DataFrame(data[1:], index=['names', 'description', 'link'])
df = df.T
