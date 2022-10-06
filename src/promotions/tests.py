from django.test import TestCase
from django.test import Client


# Create your tests here.
class PromotionModelTests(TestCase):
    client = None
    url = '/promotions/'
    payload = {
        'label': 'Add unit test'
    }

    update_payload = {
        'id': 1,
        'label': 'Update unit test'
    }

    expected_add_payload = {
        'code': 200,
        'result': 'success',
        'data': {
            'id': 2,
            'label': 'Add unit test'
        }
    }

    expected_update_payload = {
        'code': 200,
        'result': 'success',
        'data': {
            'id': 1,
            'label': 'Update unit test'
        }
    }

    expected_get_promotions_payload = {
        'code': 200,
        'result': 'success',
        'data': [
            {
                'id': 1,
                'label': 'Add unit test'
            }
        ]
    }

    expected_get_promotion_payload = {
        'code': 200,
        'result': 'success',
        'data': {
            'id': 1,
            'label': 'Add unit test'
        }
    }

    expected_delete_payload = {
        "code": 200,
        "result": "success",
        "data": []
    }

    expected_404_on_label = {
        "code": 404,
        "result": "error",
        "message": "Could not save the data",
        "data": {
            "label": [
                "This field is required."
            ]
        }
    }

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.client.post(cls.url + 'add', cls.payload, 'application/json')

    def test01_create_promotion(self):
        path = self.url + 'add'

        response = self.client.post(path, self.payload, 'application/json')
        self.assertEqual(response.json(), self.expected_add_payload)

    def test02_get_promotion(self):
        path = self.url + '1'
        response = self.client.get(path)
        self.assertEqual(response.json(), self.expected_get_promotion_payload)

    def test03_get_promotions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.json(), self.expected_get_promotions_payload)

    def test04_update_promotion(self):
        path = self.url + 'update'

        response = self.client.patch(path, self.update_payload, 'application/json')
        self.assertEqual(response.json(), self.expected_update_payload)

    def test05_delete_promotion(self):
        path = self.url + 'delete/1'

        response = self.client.delete(path)
        self.assertEqual(response.json(), self.expected_delete_payload)

    def test_06_create_promotion_with_empty_array_on_label(self):
        path = self.url + 'add'
        payload = {
            'label': []
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_label)

    def test_06_create_promotion_with_empty_object_on_label(self):
        path = self.url + 'add'
        payload = {
            'label': {}
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_label)

