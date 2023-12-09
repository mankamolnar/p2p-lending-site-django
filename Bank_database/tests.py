from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from Bank_database.models import Szamla , Kerelem
from urllib.parse import urlencode



#Import for logging:
import logging

logger = logging.getLogger('Test_logger')


class HomepageTest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_homepage(self):
        response = self.client.get(reverse("main_page"))
        logger.debug("Semmi2")

        self.assertEqual(response.status_code, 200)
        self.assertTrue("<title>" in str(response.content))

    def test_homepage_authenticated_user(self):
        user = User.objects.create(username="testjani")
        user.set_password("testme")
        user.save()

        szamla = Szamla(aktualis_osszeg=9999, szamla_tulajdonos=user, szamla_tipus="Investor")
        szamla.save()

        self.client.login(username="testjani", password="testme")
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTrue("<p>Welcome to the site testjani</p>" in str(response.content))

    def test_szamla_osszeg(self):
        #given
        user = User.objects.create(username="testjani")
        user.set_password("testme")
        user.save()
        szamla = Szamla(aktualis_osszeg=9999, szamla_tulajdonos=user, szamla_tipus="Investor")
        szamla.save()
        #when
        self.client.login(username="testjani", password="testme")
        response = self.client.get("/")
        #then:
        self.assertTrue("<td>9999.0</td>" in  str(response.content))


class LendingListTest(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_list_autentication_test(self):
        #giveb
        user = User.objects.create(username="Testuser")
        user.set_password("testuserpassword")
        szamla = Szamla(aktualis_osszeg=9999, szamla_tulajdonos=user, szamla_tipus="Investor")
        user.save()
        szamla.save()
        lending = Kerelem(osszeg = 100, futamido = 1, kamat = 10,leiras = "valami",felvett=False,szamla=szamla,torlesztett = False)
        lending.save()
        #when:
        self.client.login(username="Testuser", password="testuserpassword")
        response = self.client.get(reverse("list_lendings"))
        #then:
        self.assertTrue("<td>100.0</td>" in str(response.content))
        self.assertTrue("<td>1</td>" in str(response.content))
        self.assertTrue("<td>10.0</td>" in str(response.content))
        self.assertTrue("<td>False</td>" in str(response.content))
        self.assertTrue("<td>valami</td>" in str(response.content))

class RegistrationTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form(self):
        response = self.client.get(reverse('registration'))
        self.assertTrue('<input type="password" name="password1" autocomplete="new-password" class="form-control" id="floatingPassword1" required>' in str(response.content))
        self.assertTrue('<form method="post" action="/registration/">' in str(response.content))

    def test_registration_of_user(self):
        #given:
        data = urlencode({"username": "Feri",
                          "password1": "abc123efg544",
                          "password2": "abc123efg544",
                          "account_type":"Investor",
                          })
        #when:
        response = self.client.post(reverse("registration"), data, content_type="application/x-www-form-urlencoded")
        #then:
        
        user_check = User.objects.filter(username = "Feri").exists()
        self.assertTrue(user_check)

    def test_wrong_registration(self):
        #given:
        data = urlencode({"username": "Béla",
                          "password1": "abc123efg544",
                          "password2": "sdsd",
                          "account_type":"Investor",
                          })
        #when:
        response = self.client.post(reverse("registration"), data, content_type="application/x-www-form-urlencoded")
        #then:
        self.assertTrue("Form is not correct, there are errors in the form." in str(response.content))

class LoginTest(TestCase):
    def setUp(self) -> None:
            self.client = Client()


    def test_login_form(self):
        #given:

        #when:
        response = self.client.get(reverse("custom_login"))
        #then:
        self.assertTrue('<form method="post" action="/accounts/login/">' in str(response.content))

    def test_login(self):
        #given:
        user = User.objects.create(username="Béla")
        user.set_password("abc123efg544")
        szamla = Szamla(aktualis_osszeg=9999, szamla_tulajdonos=user, szamla_tipus="Investor")
        user.save()
        szamla.save()


        data = urlencode({"username": "Béla",
                    "password": "abc123efg544",
                    })
        
        #when 
        response = self.client.post(reverse("login"),data, content_type="application/x-www-form-urlencoded")
        #then:
        self.assertRedirects(response, reverse("main_page"),status_code=302 ,target_status_code=200)
        #How to check redirect webpages:


    def test_login_error(self):
        data = urlencode({"username": "Béla",
                    "password": "abc123efg544",
                    })
        response = self.client.post(reverse("login"),data, content_type="application/x-www-form-urlencoded")

        self.assertTrue('<p class="error">Error happend during login</p>' in str(response.content))

class TestMainPage(TestCase):
    def setUp(self) -> None:
        self.client = Client()


    def test_main_view_unlogged(self):
        #given:

        #when:
        response = self.client.get(reverse("main_page"))
        #then:
        self.assertTrue("<h1>Welcome in The Trading site!</h1>" in str(response.content))

    def test_main_view_logged(self):
        #given: 
        user = User.objects.create(username = "testjani")
        user.set_password("testme")
        user.save()


        szamla = Szamla(aktualis_osszeg=9999, szamla_tulajdonos=user, szamla_tipus="Investor")
        szamla.save()


        #when:
        self.client.login(username="testjani", password="testme")
        response = self.client.get(reverse("main_page"))
        #then:
        self.assertTrue("<td>testjani</td>" in str(response.content))
        self.assertTrue("<td>9999.0</td>" in str(response.content))
        self.assertTrue("<td>Investor</td>" in str(response.content))


class TestAddBalance(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def view_form(self):
        #given:

        #when:
        response = self.client.get(reverse("add_currency"))
        #then:
        self.assertTrue('<form method="post">' in str(response.content))

    def test_adding_money_to_balance(self):
        #given:
        user = User.objects.create(username = "testjani")
        user.set_password("testme")
        user.save()

        szamla = Szamla(aktualis_osszeg=9999, szamla_tulajdonos=user, szamla_tipus="Investor")
        szamla.save()

        data =  urlencode({
                            "szamla_id" : user.id,
                            "osszeg": "1",
                            "tranzakcio_fajta":"Befizetés"
                          })
        #when:
        self.client.login(username="testjani", password="testme")
        reponse = self.client.post(reverse("add_currency"),data,content_type="application/x-www-form-urlencoded")

        #then:
        self.assertTrue("<td>10000.0</td>" in str(reponse.content))


class TestLendMoneySite(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        user = User.objects.create(username = "testjani")
        user.set_password("testme")
        user.save()

        szamla = Szamla(aktualis_osszeg=9999, szamla_tulajdonos=user, szamla_tipus="Investor")
        szamla.save()


    def test_view_of_lend_site(self):
        #given:
        self.client.login(username = "testjani", password = "testme")

        #when?:
        response = self.client.get(reverse('lend_money'))
        #then:
        self.assertTrue('<form method="POST">' in str(response.content))
        print()
        self.assertTrue('<input type="number" name="osszeg"' in str(response.content))
        self.assertTrue('<input type="number" name="futamido" ' in str(response.content))
        self.assertTrue('' in str(response.content))
        self.assertTrue('' in str(response.content))
        self.assertTrue('' in str(response.content))

        #Folytatás kövi:
        # log formba


        

        



    



    
        
                                        


