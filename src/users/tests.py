from django.http import HttpRequest, HttpResponse
from django.test import TestCase
from django.test import Client

from .models import Member


# Create your tests here.
class MemberModelTests(TestCase):
    member_id = None,
    host = '0.0.0.0'
    port = '8000'
    url = '/users/'
    payload = {
        'firstname': "Add",
        'lastname': "UnitTest",
        'email': "add.unittest@gmail.com",
        'promo': 1
    }

    def test_create_member(self):
        path = self.url + 'add'

        request = Client()
        role = request.post('roles/add', {'label': 'testAddInCreateMember'}, 'application/json')
        print(role.json())
        response = request.post(path, self.payload, 'application/json')
        print(response.json())

