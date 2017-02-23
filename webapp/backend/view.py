from django.http import JsonResponse
import pymongo


def api_test(request):
    return JsonResponse({'code': 200})


def api_hackernews(request):
    client = pymongo.MongoClient()
    db = client.test
    col = db.hackernews

    data = list()

    for doc in col.find():
        doc.pop('_id')
        data.append(doc)

    return JsonResponse(data, safe=False)


def api_github(request):
    client = pymongo.MongoClient()
    db = client.test
    col = db.github

    data = list()

    for doc in col.find():
        doc.pop('_id')
        data.append(doc)

    return JsonResponse(data, safe=False)