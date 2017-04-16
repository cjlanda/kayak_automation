from BaseTestCase import BaseTestCase
from configurations.Config import Configurations
from pageObjects.Hotels_PageObject import Hotels_PageObject
import time

import unittest

class SmokeTest(BaseTestCase, unittest.TestCase):
    def setUp(self):
        super(SmokeTest, self).setUp()
        self.navigate_to_page(Configurations['Base_URL'])

    def test_QueryMissingCheckInDate(self):
        """
        Test to query Hotels in San Francisco without Entering Check-In Date.
        """
        hotels_page_obj = Hotels_PageObject(self.driver)
        hotels_page_obj.whereInput("San Francisco")
        hotels_page_obj.pressSearch()
        assert "Please enter a check-in date." == hotels_page_obj.getAlertMessage()
        hotels_page_obj.acceptAlertMessage()

    def tearDown(self):
        super(SmokeTest, self).tearDown()

if __name__ == "__main__":
    unittest.main()