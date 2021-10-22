from django.test import TestCase, Client
from django.core.cache import cache

from apps.accounts.models import Account


class AccountTest(TestCase):
    """General Tests for Accounts Verification"""

    def setUp(self):
        """Fixtures"""

        self.username = 'new_user'
        self.username2 = 'new_user2'
        self.role = 'Administrator'
        self.email = 'newuser@university-schedule.com'
        self.email2 = 'newuser2@university-schedule.com'
        self.passwd = '1234'

        # create an object of class Client (), web browser emulator (authorized)
        self.auth_client = Client()
        # create an object of class Client (), web browser emulator (unauthorized)
        self.unauth_client = Client()
        # create ACCOUNT objects (authorized / unauthorized)
        self.user_auth = Account.objects.create(
            username=self.username2,
            password=self.passwd,
            email=self.email2,
            is_active=True,
            is_staff=True,
            role=self.role,
        )
        self.user_unauth = Account.objects.create(username='anonimus')

        # emulation of authorization for self.user_auth
        self.auth_client.force_login(self.user_auth)
        # clear cache before running tests
        cache.clear()

    def test_model_user(self):
        """test for checking the Account model"""

        # requests for the initial number of ACCOUNT objects
        total_count_obj = Account.objects.all().count()
        total_count_obj2 = Account.objects.filter(username=self.username).count()
        # checking the number of objects ACCOUNT
        self.assertEqual(2, total_count_obj)
        self.assertEqual(0, total_count_obj2)
        # creating a new user and checking
        new_user = Account.objects.create(username=self.username, role=self.role, email=self.email)
        self.assertEqual(new_user.username, self.username)
        self.assertEqual(new_user.role, self.role)
        self.assertEqual(new_user.email, self.email)
        # queries for the number of ACCOUNT objects after creating a new one and checking
        now_total_count_obj = Account.objects.all().count()
        now_total_count_obj2 = Account.objects.filter(username=self.username).filter(email=self.email).count()
        self.assertEqual(now_total_count_obj, total_count_obj + 1)
        self.assertEqual(now_total_count_obj2, total_count_obj2 + 1)
        # queries from the database and checking a new user
        get_user = Account.objects.get(username=self.username, email=self.email)
        self.assertEqual(get_user.username, self.username)
        self.assertEqual(get_user.role, self.role)
        self.assertEqual(get_user.email, self.email)

    def test_login_auth_user(self):
        """test for checking login by an authorized user"""

        # check login from admin panel
        response = self.auth_client.post('/secureadmin/', {'username': self.username2, 'password': self.passwd})
        self.assertEqual(response.status_code, 200)

        # # logout
        # self.auth_client.logout()
        # # checking the authorization of the registered user
        # response2 = self.auth_client.login(email=self.email2, password=self.passwd)
        # self.assertEqual(response2, True)

    def test_login_unauth_user(self):
        """test for checking login by unauthorized user"""

        response = self.unauth_client.login(username='anonimus', password=self.passwd)
        self.assertEqual(response, False)


class PageTest(TestCase):
    """Common tests for checking pages"""

    def setUp(self):
        """Fixtures"""

        self.username = 'new_user'
        self.role = 'User'
        self.email = 'newuser@crm.com'
        self.passwd = '1234'
        self.auth_client = Client()
        self.unauth_client = Client()
        self.user_auth = Account.objects.create(username=self.username, password=self.passwd, email=self.email)
        self.user_unauth = Account.objects.create(username='anonimus')
        self.auth_client.force_login(self.user_auth)
        cache.clear()

    def test_index_page(self):
        """home page request test"""

        response = self.auth_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin_page(self):
        """admin page request test"""

        response = self.auth_client.get('/secureadmin/')
        self.assertEqual(response.status_code, 302)

    def test_404_page(self):
        """404 error request test"""

        response = self.auth_client.get('/stud/', follow=True)
        self.assertEqual(response.status_code, 404)
