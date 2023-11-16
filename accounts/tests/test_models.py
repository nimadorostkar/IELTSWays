from django.test import TestCase
from accounts.models import User


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {'national_id':'1234567890', 'password':'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/accounts/login', self.credentials, follow=True)
        response = response.json()
        # should be logged in now
        self.assertTrue(response['data']['user_data']['is_active'])


