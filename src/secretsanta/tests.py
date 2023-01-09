from django.test import Client
from django.test import TestCase


class SecretSantaTests(TestCase):
    client = None
    # Base URL
    BASE_URL = '/santa/'

    # Create secret santa payload
    CREATE_SANTA_PAYLOAD = {
        "label": "Test secret santa - First",
        "description": "This is a secret santa description",
        "draw_date": "2022-10-10",
    }

    CREATE_OTHER_SANTA_PAYLOAD = {
        "label": "Test secret santa - Second",
        "description": "This is a secret santa description",
        "draw_date": "2022-10-10",
    }

    # Update secret santa payload
    UPDATE_SANTA_PAYLOAD = {
        "label": "Update secret santa",
        "description": "This is an update in secret santa description",
        "draw_date": "2021-10-10",
    }

    # Body when create santa
    BODY_CREATE_SANTA = {
        "code": 200,
        "result": "success",
        "data": {
            "id": 2,
            "label": "Test secret santa - Second",
            "description": "This is a secret santa description",
            "draw_date": "2022-10-10T00:00:00Z"
        },
    }

    # Body when fetching all secret santa
    BODY_GET_SANTAS = {
        "code": 200,
        "result": "success",
        "data": [
            {
                "id": 1,
                "label": "Test secret santa - First",
                "description": "This is a secret santa description",
                "draw_date": "2022-10-10T00:00:00Z",
            }
        ],
    }

    # Body after fetching one secret santa
    BODY_GET_SANTA = {
        "code": 200,
        "result": "success",
        "data": {
            "id": 1,
            "label": "Test secret santa - First",
            "description": "This is a secret santa description",
            "draw_date": "2022-10-10T00:00:00Z",
        },
    }

    # Body after update specific secret santa
    BODY_UPDATE_SANTA = {
        "code": 200,
        "result": "success",
        "data": {
            "id": 1,
            "label": "Update secret santa",
            "description": "This is an update in secret santa description",
            "draw_date": "2021-10-10T00:00:00Z",
        },
    }

    # Body after delete specific secret santa
    BODY_DELETE_SANTA = {
        "code": 200,
        "result": "success",
        "data": []
    }

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.client.post(
            cls.BASE_URL + 'add', cls.CREATE_SANTA_PAYLOAD, 'application/json')

    def test01_create_santa(self):
        response = self.client.post(
            self.BASE_URL + 'add', self.CREATE_OTHER_SANTA_PAYLOAD, 'application/json')
        self.assertEqual(response.json(), self.BODY_CREATE_SANTA)

    def test02_get_santa(self):
        response = self.client.get(self.BASE_URL + '1')
        self.assertEqual(response.json(), self.BODY_GET_SANTA)

    def test03_get_santas(self):
        response = self.client.get(self.BASE_URL)
        self.assertEqual(response.json(), self.BODY_GET_SANTAS)

    def test04_update_santa(self):
        response = self.client.patch(
            self.BASE_URL + 'update/1', self.UPDATE_SANTA_PAYLOAD, 'application/json')
        self.assertEqual(response.json(), self.BODY_UPDATE_SANTA)

    def test05_delete_santa(self):
        response = self.client.delete(self.BASE_URL + 'delete/1')
        self.assertEqual(response.json(), self.BODY_DELETE_SANTA)
