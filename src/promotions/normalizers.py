from .models import Promotion


def promotions_normalizer(data):
    result = []
    for promotion in data:
        item = {
            'id': promotion['id'],
            'label': promotion['label'],
        }

        result.append(item)

    return result


def promotion_normalizer(data):
    return {
        'id': data.id,
        'label': data.label,
    }

