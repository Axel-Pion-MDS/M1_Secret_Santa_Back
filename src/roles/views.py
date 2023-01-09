import django.middleware.csrf
import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import RoleForm
from .models import Role
from .normalizers import roles_normalizer, role_normalizer


# Create your views here.
@csrf_exempt
def get_roles(request):
    if request.method == 'GET':
        roles = Role.objects.all().values()

        if roles:
            data = roles_normalizer(roles)
        else:
            return JsonResponse({'code': 200, 'result': 'success', 'data': []})
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def get_role(request, role_id):
    if request.method == "GET":
        try:
            role = Role.objects.get(pk=role_id)
        except Role.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Role not found.'})

        data = role_normalizer(role)
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a GET method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def add_role(request):
    if request.method == "POST":
        decode = request.body.decode('utf-8')
        content = json.loads(decode)
        form = RoleForm(content)

        if form.is_valid():
            form.save()
            data = role_normalizer(Role.objects.latest('id'))
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
def update_role(request):
    if request.method == 'PATCH':
        decode = request.body.decode('utf-8')
        content = json.loads(decode)
        role_id = content['id']

        try:
            role = Role.objects.get(pk=role_id)
        except Role.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Role not found.'})

        form = RoleForm(instance=role, data=content)

        if form.is_valid():
            role.save()
        else:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Could not save the data', 'data': form.errors})

    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a PATCH method', 'data': []})

    data = role_normalizer(role)

    return JsonResponse({'code': 200, 'result': 'success', 'data': data})


@csrf_exempt
def delete_role(request, role_id):
    if request.method == 'DELETE':
        try:
            role = Role.objects.get(pk=role_id)
        except Role.DoesNotExist:
            return JsonResponse({'code': 404, 'result': 'error', 'message': 'Role not found.'})

        role.delete()
    else:
        return JsonResponse({'code': 403, 'result': 'forbidden', 'message': 'Must be a DELETE method', 'data': []})

    return JsonResponse({'code': 200, 'result': 'success', 'data': []})
