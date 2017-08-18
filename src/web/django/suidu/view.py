from django.http import JsonResponse
import pymongo
import os

def test(request):
    mongo_url = os.environ.get("MONGODB_PORT_27017_TCP_ADDR") + ":" + os.environ.get("MONGODB_PORT_27017_TCP_PORT")
    client = pymongo.MongoClient(mongo_url)
    db = client.test
    col = db.test
    data = []
    for doc in col.find():
        doc.pop('_id')
        data.append(doc)
    return JsonResponse(data, safe=False)