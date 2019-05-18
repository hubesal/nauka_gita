import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['app'] = PATH('C:\APP\ContactManager.apk')   #uwaga nowa aplikacja ContactManager.apk
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def testAddContact(self):

        addContactBtn = self.driver.find_element_by_accessibility_id("Add Contact")
        sleep(2)
        addContactBtn.click()
        sleep(2)
        textFields = self.driver.find_elements_by_class_name("android.widget.EditText")
        sleep(2)
        textFields[0].send_keys("Tester")
        textFields[1].send_keys("1234567890")
        textFields[2].send_keys("tester@test.com")

        for text in textFields:
            print text
        sleep(2)
        el = self.driver.find_element_by_class_name("android.widget.Button")
        sleep(2) 
        el.click()