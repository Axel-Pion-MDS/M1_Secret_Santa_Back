from django.http import HttpResponse

from .models import Member


def members_normalizer(data):
    result = []
    for member in data:
        member_details = Member.objects.get(pk=member['id'])

        item = {
            'id': member['id'],
            'firstname': member['firstname'],
            'lastname': member['lastname'],
            'email': member['email'],
            'promotion': {
                'id': member_details.promo.id,
                'label': member_details.promo.label,
            } if member_details.promo else 'null',
            'role': {
                'id': member_details.role.id,
                'label': member_details.role.label,
            } if member_details.role else 'null',
        }

        result.append(item)

    return result


def member_normalizer(data):
    return {
        'id': data.id,
        'firstname': data.firstname,
        'lastname': data.lastname,
        'email': data.email,
        'promotion': {
            'id': data.promo.id,
            'label': data.promo.label,
        } if data.promo else 'null',
        'role': {
            'id': data.role.id,
            'label': data.role.label,
        } if data.role else 'null',
    }

