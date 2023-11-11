from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from Bank_database.models import Szamla


class OsszeadasTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get(reverse("main_page"))

        self.assertEqual(response.status_code, 200)
        self.assertTrue("<title>" in str(response.content))

    def test_homepage_authenticated_user(self):
        user = User.objects.create(username="testjani")
        user.set_password("testme")
        user.save()

        szamla = Szamla(aktualis_osszeg=0, szamla_tulajdonos=user, szamla_tipus="Investor")
        szamla.save()

        self.client.login(username="testjani", password="testme")
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTrue("<p>Welcome to the site testjani</p>" in str(response.content))
