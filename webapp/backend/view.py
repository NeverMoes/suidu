from django.http import JsonResponse


def api_test(request):
    return JsonResponse({'code': 200})