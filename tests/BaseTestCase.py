from selenium import webdriver
from configurations.Config import Configurations

class BaseTestCase(object):

  def setUp(self):

    if Configurations['Browser'].lower() == "chrome":
        self.driver = webdriver.Chrome('drivers/chromedriver')
    else:
        print("this browser is not yet supported.")

  def navigate_to_page(self, url):
      self.driver.get(url)

  def tearDown(self):
      self.driver.quit()

