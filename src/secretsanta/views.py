import json

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse

from .models import Santa, SantaMember
from .forms import SantaForm, SantaMemberForm, SantaMemberUpdateForm
from .normalizer import santa_normalizer, santas_normalizer, santa_members_normalizer, santa_member_normalizer

#
# Santa
#


@csrf_exempt
def get_santas(request):
    if request.method == "GET":
        try:
            query = Santa.objects.all()
            data = santas_normalizer(query)
        except Santa.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Secret santa not found.'})
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def get_active_santas(request):
    if request.method == "GET":
        import datetime
        current_date = datetime.datetime.now()
        try:
            query = Santa.objects.all().filter(draw_date__gt=current_date)
            data = santas_normalizer(query)
        except Santa.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Secret santa not found.'})
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def get_santa(request, santa_id):
    if request.method == "GET":
        try:
            query = Santa.objects.get(pk=santa_id)
            data = santa_normalizer(query)
        except Santa.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Secret santa not found.'})
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def add_santa(request):
    if request.method == "POST":
        decode = request.body.decode('utf-8')
        body = json.loads(decode)
        form = SantaForm(body)

        if form.is_valid():
            form.save()
            data = santa_normalizer(Santa.objects.latest('id'))
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
def update_santa(request, santa_id):
    if request.method == 'PATCH':
        decode = request.body.decode('utf-8')
        content = json.loads(decode)

        try:
            santa = Santa.objects.get(pk=santa_id)
        except Santa.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Secret santa not found.', 'data': []})

        form = SantaForm(instance=santa, data=content)

        if form.is_valid():
            santa.save()
        else:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Error in form.', 'data': form.errors})

    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a PATCH method', 'data': []})

    data = santa_normalizer(santa)

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def delete_santa(request, santa_id):
    if request.method == "DELETE":
        try:
            santa = Santa.objects.get(id=santa_id)
        except Santa.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Secret santa not found.'})

        santa.delete()
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': []})


#
# Santa members
#


@csrf_exempt
def get_santa_members(request, santa_id):
    if request.method == "GET":
        query = SantaMember.objects.all().filter(santa_id=santa_id)
        if query:
            data = santa_members_normalizer(query)
        else:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'No members found in this secret santa.'})
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def get_santa_member(request, santa_id, member_id):
    if request.method == "GET":
        query = SantaMember.objects.all().filter(
            santa_id=santa_id).filter(member_id=member_id)
        if query:
            data = santa_member_normalizer(query[0])
        else:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'No members found in this secret santa.'})
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def add_santa_member(request, santa_id):
    if request.method == "POST":
        decode = request.body.decode('utf-8')
        body = json.loads(decode)

        data = {
            'santa': santa_id,
            'member': body['member'],
            'target': body['target'],
        }

        form = SantaMemberForm(data)

        if form.is_valid():
            form.save()
            data = santa_member_normalizer(SantaMember.objects.latest('id'))
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
def update_santa_member(request, santa_id, member_id):
    if request.method == 'PATCH':
        decode = request.body.decode('utf-8')
        content = json.loads(decode)

        santa_member = SantaMember.objects.filter(
            santa_id=santa_id).filter(member_id=member_id)
        if santa_member:
            member = santa_member[0]
            data = {
                'santa': santa_id,
                'member': member_id,
                'target': content['target'],
            }

            form = SantaMemberUpdateForm(instance=member, data=data)

            if form.is_valid():
                member.save()
            else:
                return JsonResponse({'code': 404, 'result': 'error', 'message': 'Error in form.', 'data': form.errors})
        else:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Member not found.', 'data': []})

    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a PATCH method', 'data': []})

    data = santa_member_normalizer(member)

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def delete_santa_member(request, santa_id, member_id):
    if request.method == "DELETE":
        member = SantaMember.objects.filter(
            santa_id=santa_id).filter(member_id=member_id)
        if member:
            member.delete()
        else:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'No member found in this secret santa.'})

    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': []})
