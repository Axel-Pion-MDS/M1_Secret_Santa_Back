from .models import Santa
from users.models import Member

from users.normalizers import member_normalizer


def santa_normalizer(data):
    return {
        'id': data.id,
        'label': data.label,
        'description': data.description,
        'draw_date': data.draw_date,
    }


def santas_normalizer(data):
    santas = []

    for santa in data:
        item = {
            'id': santa.id,
            'label': santa.label,
            'description': santa.description,
            'draw_date': santa.draw_date,
        }
        santas.append(item)

    return santas


def santa_members_normalizer(data):
    santa = Santa.objects.get(pk=data[0].santa_id)
    members = []

    for member in data:
        member_data = Member.objects.get(pk=member.member_id)
        target_data = Member.objects.get(pk=member.target_id)

        item = {
            'member': member_normalizer(member_data),
            'target': member_normalizer(target_data),
        }

        members.append(item)

    return {
        'santa': santa_normalizer(santa),
        'members': members
    }


def santa_member_normalizer(data):
    santa = Santa.objects.get(pk=data.santa_id)
    member = Member.objects.get(pk=data.member_id)
    target = Member.objects.get(pk=data.target_id)

    return {
        'santa': santa_normalizer(santa),
        'member': member_normalizer(member),
        'target': member_normalizer(target),
    }
