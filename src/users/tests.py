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
        'promo': 1,
        'santa': 1
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

    expected_404_on_member = {
        "code": 404,
        "result": "error",
        "message": "Member not found."
    }

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.client.post('/santa/add', {
            "label": "UnitTestSanta",
            "description": "This is a description for a secret santa",
            "draw_date": "2022-12-22T00:00:00.000Z"
        }, 'application/json')
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

    def test05_create_member_with_empty_array_on_firstname(self):
        path = self.url + 'add'
        payload = {
            'firstname': [],
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "firstname": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test06_create_member_with_empty_array_on_lastname(self):
        path = self.url + 'add'
        payload = {
            'firstname': "Add",
            'lastname': [],
            'email': "add.unittest@gmail.com",
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "lastname": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test07_create_member_with_empty_array_on_email(self):
        path = self.url + 'add'
        payload = {
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': [],
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "email": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test08_create_member_with_empty_array_on_promo(self):
        path = self.url + 'add'
        payload = {
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promo': [],
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "promo": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test09_create_member_with_empty_object_on_firstname(self):
        path = self.url + 'add'
        payload = {
            'firstname': {},
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "firstname": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test10_create_member_with_empty_object_on_lastname(self):
        path = self.url + 'add'
        payload = {
            'firstname': "Add",
            'lastname': {},
            'email': "add.unittest@gmail.com",
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "lastname": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test11_create_member_with_empty_object_on_email(self):
        path = self.url + 'add'
        payload = {
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': {},
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "email": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test12_create_member_with_empty_object_on_promo(self):
        path = self.url + 'add'
        payload = {
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promo': {},
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "promo": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test13_create_member_with_empty_payload(self):
        path = self.url + 'add'
        payload = {}

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "firstname": [
                    "This field is required."
                ],
                "lastname": [
                    "This field is required."
                ],
                "email": [
                    "This field is required."
                ],
                "promo": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test14_update_member_with_wrong_id(self):
        path = self.url + 'update'
        payload = {
            'id': 666,
            'firstname': "Update",
            'lastname': "UnitTest",
            'email': "update.unittest@gmail.com",
            'promo': 1
        }

        response = self.client.patch(path, payload, 'application/json')
        self.assertEqual(response.json(), self.expected_404_on_member)

    def test15_update_member_with_empty_array_on_firstname(self):
        path = self.url + 'add'
        payload = {
            'id': 1,
            'firstname': [],
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "firstname": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test16_update_member_with_empty_array_on_lastname(self):
        path = self.url + 'add'
        payload = {
            'id': 1,
            'firstname': "Add",
            'lastname': [],
            'email': "add.unittest@gmail.com",
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "lastname": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test17_update_member_with_empty_array_on_email(self):
        path = self.url + 'add'
        payload = {
            'id': 1,
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': [],
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "email": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test18_update_member_with_empty_array_on_promo(self):
        path = self.url + 'add'
        payload = {
            'id': 1,
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promo': [],
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "promo": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test19_update_member_with_empty_object_on_firstname(self):
        path = self.url + 'add'
        payload = {
            'id': 20,
            'firstname': {},
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "firstname": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test21_update_member_with_empty_object_on_lastname(self):
        path = self.url + 'add'
        payload = {
            'id': 1,
            'firstname': "Add",
            'lastname': {},
            'email': "add.unittest@gmail.com",
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "lastname": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test22_update_member_with_empty_object_on_email(self):
        path = self.url + 'add'
        payload = {
            'id': 1,
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': {},
            'promo': 1,
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "email": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test23_update_member_with_empty_object_on_promo(self):
        path = self.url + 'add'
        payload = {
            'id': 1,
            'firstname': "Add",
            'lastname': "UnitTest",
            'email': "add.unittest@gmail.com",
            'promo': {},
            'santa': 1
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "promo": [
                    "This field is required."
                ]
            }
        }

        response = self.client.post(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test24_update_member_without_data(self):
        path = self.url + 'update'
        payload = {
            'id': 1,
        }

        expected_response = {
            "code": 404,
            "result": "error",
            "message": "Could not save the data",
            "data": {
                "firstname": [
                    "This field is required."
                ],
                "lastname": [
                    "This field is required."
                ],
                "email": [
                    "This field is required."
                ],
                "promo": [
                    "This field is required."
                ]
            }
        }

        response = self.client.patch(path, payload, 'application/json')
        self.assertEqual(response.json(), expected_response)

    def test24_get_member_with_wrong_id(self):
        path = self.url + '666'

        response = self.client.get(path)
        self.assertEqual(response.json(), self.expected_404_on_member)

    def test25_delete_member(self):
        path = self.url + 'delete/1'

        response = self.client.delete(path)
        self.assertEqual(response.json(), self.expected_delete_payload)

    def test26_delete_member_with_wrong_id(self):
        path = self.url + 'delete/666'

        response = self.client.delete(path)
        self.assertEqual(response.json(), self.expected_404_on_member)
