from django.test import LiveServerTestCase
from utils.tests import SeleniumUtilityBelt
from django.core.urlresolvers import reverse
from store.models import Store


class InterfaceTestCase(SeleniumUtilityBelt, LiveServerTestCase):
    def setUp(self):
        super(InterfaceTestCase, self).setUp()

    def test_empty_store_creation(self):
        count = Store.objects.count()
        url = reverse('new_store')
        self.open(url)
        button = self.driver.find_element_by_name('save')
        button.click()
        self.assertOnPage("#error_1_id_name", visible=True)
        self.assertEqual(Store.objects.count(), count)

    def test_visivility_of_form(self):
        url = reverse('new_store')
        self.open(url)
        self.assertOnPage('#id_name', visible=True)
        self.assertOnPage('#id_address', visible=True)

    def test_store_creation(self):
        count = Store.objects.count()
        url = reverse('new_store')
        self.open(url)
        name = self.driver.find_element_by_name("name")
        address = self.driver.find_element_by_name("address")
        name.send_keys("test")
        address.send_keys("lalala")
        button = self.driver.find_element_by_name('save')
        button.click()
        self.assertEqual(Store.objects.count(), count + 1)
