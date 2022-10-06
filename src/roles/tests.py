from django.test import TestCase
from django.test import Client


# Create your tests here.
class RoleModelTests(TestCase):
    client = None
    url = '/roles/'
    payload = {
        'label': 'UNIT_TEST_ADD_ROLE'
    }

    update_payload = {
        'id': 1,
        'label': 'UNIT_TEST_UPDATE_ROLE'
    }

    expected_add_payload = {
        'code': 200,
        'result': 'success',
        'data': {
            'id': 2,
            'label': 'UNIT_TEST_ADD_ROLE'
        }
    }

    expected_update_payload = {
        'code': 200,
        'result': 'success',
        'data': {
            'id': 1,
            'label': 'UNIT_TEST_UPDATE_ROLE'
        }
    }

    expected_get_roles_payload = {
        'code': 200,
        'result': 'success',
        'data': [
            {
                'id': 1,
                'label': 'UNIT_TEST_ADD_ROLE'
            }
        ]
    }

    expected_get_role_payload = {
        'code': 200,
        'result': 'success',
        'data': {
            'id': 1,
            'label': 'UNIT_TEST_ADD_ROLE'
        }
    }

    expected_delete_payload = {
        "code": 200,
        "result": "success",
        "data": []
    }

    expected_404_on_empty_add = {
        "code": 404,
        "result": "error",
        "message": "Could not save the data",
        "data": {
            "label": [
                "This field is required."
            ]
        }
    }

    expected_404_on_role = {
        "code": 404,
        "result": "error",
        "message": "Role not found."
    }

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.client.post(cls.url + 'add', cls.payload, 'application/json')

    def test01_create_role(self):
        path = self.url + 'add'

        response = self.client.post(path, self.payload, 'application/json')
        self.assertEqual(response.json(), self.expected_add_payload)

    def test02_get_role(self):
        path = self.url + '1'
        response = self.client.get(path)
        self.assertEqual(response.json(), self.expected_get_role_payload)

    def test03_get_roles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.json(), self.expected_get_roles_payload)

    def test04_update_role(self):
        path = self.url + 'update'

        response = self.client.patch(path, self.update_payload, 'application/json')
        self.assertEqual(response.json(), self.expected_update_payload)

    def test05_create_role_with_empty_array_on_label(self):
        path = self.url + 'add'
        payload = {
            'label': []
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_empty_add)

    def test06_create_role_with_empty_object_on_label(self):
        path = self.url + 'add'
        payload = {
            'label': {}
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_empty_add)

    def test07_create_role_with_empty_payload(self):
        path = self.url + 'add'
        payload = {}

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_empty_add)

    def test08_update_role_with_wrong_id(self):
        path = self.url + 'update'
        payload = {
            'id': 666,
            'label': 'Update unit test'
        }

        response = self.client.patch(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_role)

    def test09_update_role_with_empty_array_on_label(self):
        path = self.url + 'update'
        payload = {
            'id': 1,
            'label': []
        }

        response = self.client.patch(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_empty_add)

    def test10_update_role_with_empty_object_on_label(self):
        path = self.url + 'update'
        payload = {
            'id': 1,
            'label': {}
        }

        response = self.client.patch(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_empty_add)

    def test11_update_role_without_label(self):
        path = self.url + 'update'
        payload = {
            'id': 1,
        }

        response = self.client.patch(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_empty_add)

    def test12_get_role_with_wrong_id(self):
        path = self.url + '666'

        response = self.client.get(path)
        self.assertEqual(response.json(), self.expected_404_on_role)

    def test13_delete_role(self):
        path = self.url + 'delete/1'

        response = self.client.delete(path)
        self.assertEqual(response.json(), self.expected_delete_payload)

    def test14_delete_role_with_wrong_id(self):
        path = self.url + 'delete/666'

        response = self.client.delete(path)
        self.assertEqual(response.json(), self.expected_404_on_role)
