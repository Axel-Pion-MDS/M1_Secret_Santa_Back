import json

from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from django.test import Client


# Create your tests here.
class MemberModelTests(TestCase):
    client = None
    url = '/users/'
    payload = {
        'firstname': "Add",
        'lastname': "UnitTest",
        'email': "add.unittest@gmail.com",
        'promo': 1
    }

    update_payload = {
        'id': 1,
        'firstname': "Update",
        'lastname': "UnitTest",
        'email': "update.unittest@gmail.com",
        'promo': 1
    }

    expected_add_payload = {
        'code': 200,
        'result': 'success',
        'data': {
            'id': 2,
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promotion': {
                'id': 1,
                'label': 'testAddInCreateMember'
            },
            'role': {
                'id': 1,
                'label': 'testAddInCreateMember'
            }
        }
    }

    expected_update_payload = {
        'code': 200,
        'result': 'success',
        'data': {
            'id': 1,
            'firstname': "Update",
            'lastname': "UnitTest",
            'email': "update.unittest@gmail.com",
            'promotion': {
                'id': 1,
                'label': 'testAddInCreateMember'
            },
            'role': {
                'id': 1,
                'label': 'testAddInCreateMember'
            }
        }
    }

    expected_get_members_payload = {
        "code": 200,
        "result": "success",
        "data": [
            {
                'id': 1,
                'firstname': "Add",
                'lastname': "UnitTest",
                'email': "add.unittest@gmail.com",
                'promotion': {
                    'id': 1,
                    'label': 'testAddInCreateMember'
                },
                'role': {
                    'id': 1,
                    'label': 'testAddInCreateMember'
                }
            }
        ]
    }

    expected_get_member_payload = {
        "code": 200,
        "result": "success",
        "data":  {
            'id': 1,
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promotion': {
                'id': 1,
                'label': 'testAddInCreateMember'
            },
            'role': {
                'id': 1,
                'label': 'testAddInCreateMember'
            }
        }
    }

    expected_delete_payload = {
        "code": 200,
        "result": "success",
        "data": []
    }

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.client.post('/roles/add', {'label': 'testAddInCreateMember'}, 'application/json')
        cls.client.post('/promotions/add', {'label': 'testAddInCreateMember'}, 'application/json')
        cls.client.post(cls.url + 'add', cls.payload, 'application/json')

    def test01_create_member(self):
        path = self.url + 'add'

        response = self.client.post(path, self.payload, 'application/json')
        self.assertEqual(response.json(), self.expected_add_payload)

    def test02_get_member(self):
        path = self.url + '1'
        response = self.client.get(path)
        self.assertEqual(response.json(), self.expected_get_member_payload)

    def test03_get_members(self):
        response = self.client.get(self.url)
        self.assertEqual(response.json(), self.expected_get_members_payload)

    def test04_update_member(self):
        path = self.url + 'update'

        response = self.client.patch(path, self.update_payload, 'application/json')
        self.assertEqual(response.json(), self.expected_update_payload)

    def test05_delete_member(self):
        path = self.url + 'delete/1'

        response = self.client.delete(path)
        self.assertEqual(response.json(), self.expected_delete_payload)