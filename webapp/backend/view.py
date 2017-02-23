from django.http import JsonResponse
import pymongo


def api_test(request):
    return JsonResponse({'code': 200})

def api_github(request):
    client = pymongo.MongoClient()
    db = client.test()