from library.Util import Util
import time

class Hotels_PageObject(object):

    def __init__(self, webdriver):
        self.driver = webdriver
        self.util = Util(self.driver)
        self.whereElementClass = "Common-Widgets-Text-TextInput"
        self.searchButtonClass = "searchButton"
        self.errorMessagesClass = "errorMessages"
        self.errorCloseButtonClass = "closeButton"

    def whereInput(self, input_string):
        for element in self.util.find_elements_by_class_name(self.whereElementClass):
            if element.get_attribute("placeholder") == "Where":
                element.send_keys(input_string)
                return

    def pressSearch(self):
        for element in self.util.find_elements_by_class_name(self.searchButtonClass):
            if element.text == "Search":
                element.click()
                return

    def getAlertMessage(self):
        self.driver.switch_to_alert()
        time.sleep(3)
        alertMessage = self.util.find_element_by_class_name(self.errorMessagesClass)
        if alertMessage.is_displayed():
            return alertMessage.text

    def acceptAlertMessage(self):
        okElement = self.util.find_element_by_class_name(self.errorCloseButtonClass)
        if okElement.is_displayed():
            okElement.click()







