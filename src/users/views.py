import django.middleware.csrf
import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import MemberForm
from .models import Member
from .normalizers import members_normalizer, member_normalizer
from secretsanta.models import Santa, SantaMember



# Create your views here.
@csrf_exempt
def get_members(request):
    if request.method == 'GET':
        members = Member.objects.all().values()

        if members:
            data = members_normalizer(members)
        else:
            return JsonResponse({'code': 200, 'result': 'success', 'data': []})
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def get_member(request, member_id):
    if request.method == "GET":
        try:
            member = Member.objects.get(pk=member_id)
        except Member.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Member not found.'})

        data = member_normalizer(member)
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def add_member(request):
    if request.method == "POST":
        decode = request.body.decode('utf-8')
        content = json.loads(decode)
        form = MemberForm(content)

        if form.is_valid():
            form.save()
            data = member_normalizer(Member.objects.latest('id'))

            if content['santa']:
                try:
                    santa = Santa.objects.get(pk=content['santa'])
                except Santa.DoesNotExist:
                    return JsonResponse({'code': 404, 'result': 'error', 'message': 'Santa not found.'})

                santaMember = SantaMember(member=Member.objects.latest('id'), santa=santa)
                SantaMember.save(santaMember)
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
def update_member(request):
    if request.method == 'PATCH':
        decode = request.body.decode('utf-8')
        content = json.loads(decode)
        member_id = content['id']

        try:
            member = Member.objects.get(pk=member_id)
        except Member.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Member not found.', 'data': []})

        form = MemberForm(instance=member, data=content)

        if form.is_valid():
            member.save()
        else:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Error in form.', 'data': form.errors})

    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a PATCH method', 'data': []})

    data = member_normalizer(member)

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def delete_member(request, member_id):
    if request.method == 'DELETE':
        try:
            member = Member.objects.get(pk=member_id)
        except Member.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Member not found.', 'data': []})

        member.delete()
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a DELETE method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': []})
