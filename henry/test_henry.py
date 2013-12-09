import os
import json




import selenium.webdriver as webdriver
from nose.tools import *

#This fails to run the test on windows with the error  'cannnot locate AnroidBootstrap.jar.''
# It loads the app OK onto the emulator
this_dir = os.path.dirname(__file__)
def test1():
    assert True

class TestHenry(object):

    def setup(self):

        desired_caps = {}
        desired_caps['device'] = 'Android'
        desired_caps['browserName'] = ''
        desired_caps['version'] = '4.3'
        desired_caps['app'] = os.path.join(this_dir,'henrietta-debug.apk')
        desired_caps['app-package'] = 'com.rethoughtsolutions.henrietta'
        desired_caps['app-activity'] = '.ListProductsActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self._values={}

    def teardown(self):
        self.driver.quit()

    def test_list_click(self):
        elem = find_element_by_tag(self.driver, 'TextView', "Lenovo X301")
        tap(self.driver, elem)
        elem = find_element_by_tag(self.driver, 'TextView', "Pad for the kids to scribble on.")


class TagNotFoundError(Exception):
    pass


def find_element_by_tag(driver, tag, text):
    unicode_text = unicode(text)
    for elem in driver.find_elements_by_tag_name(tag):
        if elem.text == text:
            return elem
    else:
        raise TagNotFoundError(text)

def tap(driver, element, touch_count=1):
    driver.execute_script("mobile: tap", {"touchCount":str(touch_count), 
                                          "element":element.id}) 
    