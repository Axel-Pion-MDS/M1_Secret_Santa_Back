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
        member_data = Member.objects.get(pk=member.member_id) if member.member_id is not None else None
        target_data = Member.objects.get(pk=member.target_id) if member.target_id is not None else None

        item = {
            'member': member_normalizer(member_data) if member.member_id is not None else None,
            'target': member_normalizer(target_data) if target_data is not None else None,
        }

        members.append(item)

    return {
        'santa': santa_normalizer(santa),
        'members': members
    }


def santa_member_normalizer(data):
    santa = Santa.objects.get(pk=data.santa_id)
    member = Member.objects.get(pk=data.member_id) if data.member_id is not None else None
    target = Member.objects.get(pk=data.target_id) if data.target_id is not None else None

    return {
        'santa': santa_normalizer(santa),
        'member': member_normalizer(member) if member is not None else None,
        'target': member_normalizer(target) if target is not None else None,
    }
