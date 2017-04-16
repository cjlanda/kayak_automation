
class Util():
    """
    Utility class

    """

    def __init__(self, webdriver):
        self.driver = webdriver

    def find_element_by_id(self, element_id):
        return self.driver.find_element_by_id(element_id)

    def find_element_by_class_name(self, element_class_name):
        return self.driver.find_element_by_class_name(element_class_name)

    def find_elements_by_class_name(self, element_class_name):
        return self.driver.find_elements_by_class_name(element_class_name)

    def find_element_by_tag_name(self, element_tag_name):
        return self.driver.find_element_by_tag_name(element_tag_name)

    def find_elements_by_tag_name(self, element_tag_name):
        return self.driver.find_elements_by_tag_name(element_tag_name)

    #add a wait until element is present function.