import django.middleware.csrf
import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import PromotionForm
from .models import Promotion
from .normalizers import promotions_normalizer, promotion_normalizer


# Create your views here.
@csrf_exempt
def get_promotions(request):
    if request.method == 'GET':
        promotions = Promotion.objects.all().values()

        if promotions:
            data = promotions_normalizer(promotions)
        else:
            return JsonResponse({'code': 200, 'result': 'success', 'data': []})
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def get_promotion(request, promotion_id):
    if request.method == "GET":
        try:
            promotion = Promotion.objects.get(pk=promotion_id)
        except Promotion.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Promotion not found.'})

        data = promotion_normalizer(promotion)
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def add_promotion(request):
    if request.method == "POST":
        decode = request.body.decode('utf-8')
        content = json.loads(decode)
        form = PromotionForm(content)

        if form.is_valid():
            form.save()
            data = promotion_normalizer(Promotion.objects.latest('id'))
        else:
            return JsonResponse({
                'code': 404,
                'result': 'error',
                'message': 'Could not save the data',
                'data': form.errors
            })
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a POST method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def update_promotion(request):
    if request.method == 'PATCH':
        decode = request.body.decode('utf-8')
        content = json.loads(decode)
        promotion_id = content['id']

        try:
            promotion = Promotion.objects.get(pk=promotion_id)
        except Promotion.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Promotion not found.', 'data': []})

        form = PromotionForm(instance=promotion, data=content)

        if form.is_valid():
            promotion.save()
        else:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Error in form.', 'data': form.errors})

    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a PATCH method', 'data': []})

    data = promotion_normalizer(promotion)

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def delete_promotion(request, promotion_id):
    if request.method == 'DELETE':
        try:
            promotion = Promotion.objects.get(pk=promotion_id)
        except Promotion.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Promotion not found.', 'data': []})

        promotion.delete()
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a DELETE method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': []})
