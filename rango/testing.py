import os
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings
from rango.models import ContactUs, Category, Page

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}" 





class SomeDesignedTests(TestCase):
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.rango_app_dir = os.path.join(self.project_base_dir, 'rango')
        
		
# the next five tests to make sure all the needed apps for google sign in are in the settings
    def test_is_allauth_app_configured(self):
        """
        Did you add the allauth app to your INSTALLED_APPS list?
        """
        is_app_configured = 'allauth' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The allauth app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")
		
    def test_is_allauth_account_app_configured(self):
        """
        Did you add the new allauth.account app to your INSTALLED_APPS list?
        """
        is_app_configured = 'allauth.account' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The allauth.account app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")
	
    def test_is_allauth_socialaccount_app_configured(self):
        """
        Did you add the new allauth.socialaccount app to your INSTALLED_APPS list?
        """
        is_app_configured = 'allauth.socialaccount' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The allauth.socialaccount app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")
	
    def test_is_allauth_socialaccount_providers_google_app_configured(self):
        """
        Did you add the new allauth.socialaccount.providers.google app to your INSTALLED_APPS list?
        """
        is_app_configured = 'allauth.socialaccount.providers.google' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The allauth.socialaccount.providers.google app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")
	
    def test_is_django_contrib_sites_app_configured(self):
        """
        Did you add the new django.contrib.sites app to your INSTALLED_APPS list?
        """
        is_app_configured = 'django.contrib.sites' in settings.INSTALLED_APPS
        
        self.assertTrue(is_app_configured, f"{FAILURE_HEADER}The django.contrib.sites app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")
        
        
    
        
        

class Sometests(TestCase):
#two test to make sure that login register and profile templates are available
    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.rango_templates_dir = os.path.join(self.templates_dir, 'rango')
        
    def test_templates_exist(self):
    
        profile_path = os.path.join(self.rango_templates_dir, 'profile.html')
        register_path = os.path.join(self.rango_templates_dir, 'register.html')
        login_path = os.path.join(self.rango_templates_dir, 'login.html')
        
        self.assertTrue(os.path.isfile(profile_path), f"{FAILURE_HEADER}Your profile.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(register_path), f"{FAILURE_HEADER}Your register.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")
        self.assertTrue(os.path.isfile(login_path), f"{FAILURE_HEADER}Your login.html template does not exist, or is in the wrong location.{FAILURE_FOOTER}")


        
        
class TestsForContact_us_model(TestCase):
    def setUp(self):
        contactus1 = ContactUs.objects.get_or_create(name='Amjad', subject='sidawi')
        
    def test_contact_us_model(self):
        """
        Runs two tests on the Contact us model.
        Do the correct attributes exist?
        """
        contactus1 = ContactUs.objects.get(name='Amjad')

        self.assertEqual(contactus1.name, 'Amjad', f"{FAILURE_HEADER}Tests on the ContactUs model failed. Check you have 'name' attribute.{FAILURE_FOOTER}")
        self.assertEqual(contactus1.subject, "sidawi", f"{FAILURE_HEADER}Tests on the ContactUs model failed. Check you have 'subject' attribute.{FAILURE_FOOTER}")

     
    

        
        
#I only wrote three class because for unknown reason It didn't work in one class    
class PopulationScriptTests(TestCase):
    """
    Tests whether the population script puts the expected data into a test database.
    """
    def setUp(self):
        """
        Imports and runs the population script, calling the populate() method.
        """
        try:
            import populate_rango
        except ImportError:
            raise ImportError(f"{FAILURE_HEADER}tests could not import the populate file. Check it's in the right location (the main directory).{FAILURE_FOOTER}")
        
        if 'populate' not in dir(populate_rango):
            raise NameError(f"{FAILURE_HEADER}The populate() function does not exist in the populate module. This is required.{FAILURE_FOOTER}")
        
        # Call the population script -- any exceptions raised here do not have fancy error messages to help readers.
        populate_rango.populate()
    
    def test_categories(self):
        """
        There should be five categories from populate_rango -- Action, Science Fiction, Drama,Animation and Comedy.
        """
        categories = Category.objects.filter()
        categories_len = len(categories)
        categories_strs = map(str, categories)
        
        self.assertEqual(categories_len, 5, f"{FAILURE_HEADER}Expecting 5 categories to be created from the populate_rango module; found {categories}.{FAILURE_FOOTER}")
        self.assertTrue('Action' in categories_strs, f"{FAILURE_HEADER}The category 'Action' was expected but not created by populate_rango.{FAILURE_FOOTER}")
        self.assertTrue('Science Fiction' in categories_strs, f"{FAILURE_HEADER}The category 'Science Fiction' was expected but not created by populate_rango.{FAILURE_FOOTER}")
        self.assertTrue('Drama' in categories_strs, f"{FAILURE_HEADER}The category 'Drama' was expected but not created by populate_rango.{FAILURE_FOOTER}")
                
        
        
class PopulationScriptTests2(TestCase):
    """
    Tests whether the population script puts the expected data into a test database.
    """
    def setUp(self):
        """
        Imports and runs the population script, calling the populate() method.
        """
        try:
            import populate_rango
        except ImportError:
            raise ImportError(f"{FAILURE_HEADER}tests could not import the populate file. Check it's in the right location (the main directory).{FAILURE_FOOTER}")
        
        if 'populate' not in dir(populate_rango):
            raise NameError(f"{FAILURE_HEADER}The populate() function does not exist in the populate module. This is required.{FAILURE_FOOTER}")
        
        # Call the population script -- any exceptions raised here do not have fancy error messages to help readers.
        populate_rango.populate()
    
    def test_categories(self):
        """
        There should be five categories from populate_rango -- Action, Science Fiction, Drama,Animation and Comedy.
        """
        categories = Category.objects.filter()
        categories_len = len(categories)
        categories_strs = map(str, categories)
        
       
        self.assertTrue('Animation' in categories_strs, f"{FAILURE_HEADER}The category 'Animation' was expected but not created by populate_rango.{FAILURE_FOOTER}")
        
class PopulationScriptTests3(TestCase):
    """
    Tests whether the population script puts the expected data into a test database.
    """
    def setUp(self):
        """
        Imports and runs the population script, calling the populate() method.
        """
        try:
            import populate_rango
        except ImportError:
            raise ImportError(f"{FAILURE_HEADER}tests could not import the populate file. Check it's in the right location (the main directory).{FAILURE_FOOTER}")
        
        if 'populate' not in dir(populate_rango):
            raise NameError(f"{FAILURE_HEADER}The populate() function does not exist in the populate module. This is required.{FAILURE_FOOTER}")
        
        # Call the population script -- any exceptions raised here do not have fancy error messages to help readers.
        populate_rango.populate()
    
    def test_categories(self):
        """
        There should be five categories from populate_rango -- Action, Science Fiction, Drama,Animation and Comedy.
        """
        categories = Category.objects.filter()
        categories_len = len(categories)
        categories_strs = map(str, categories)
        
       
        self.assertTrue('Comedy' in categories_strs, f"{FAILURE_HEADER}The category 'Comedy' was expected but not created by populate_rango.{FAILURE_FOOTER}")
        
        
        

        
