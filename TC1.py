import os
import unittest
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('C:\APP\ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_accesibility_button(self):
        accButton1 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Preference"]')
       # print(accButton1)
        accButton1.click()
        sleep(2)
        accButton2 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="3. Preference dependencies"]')
        sleep(2)
        accButton2.click()
        checkBoxes = self.driver.find_elements_by_android_uiautomator('new UiSelector().checkable(true)')
        checkBoxes[0].click()

#        if (checkBoxes[0].get_attribute("checked")):
#           print("nothing to click")
#        else:
#            checkBoxes[0].click()

        accButton3 = self.driver.find_element_by_xpath('//android.widget.TextView[@text="WiFi settings"]')
        sleep(2)
        accButton3.click()
        sleep(2)
        formField = self.driver.find_element_by_xpath('//android.widget.ScrollView[@index="0"]')
        formField.send_keys("123456")
        sleep(2)
        OKButton = self.driver.find_element_by_xpath('//android.widget.TextView[@text="OK"]')
        OKButton.click()
        sleep(5)
        self.driver.keyevent(4)