import pymongo
import datetime

client = pymongo.MongoClient()
db = client.suidu
col = db.test

today = datetime.date.today()
date = datetime.datetime(today.year, today.month, today.day)

data = {
    "time": date,
}


col.insert(data)