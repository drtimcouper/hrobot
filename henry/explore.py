import os

import selenium.webdriver as webdriver

this_dir = os.path.dirname(__file__)


desired_caps = {}
desired_caps['device'] = 'Android'
desired_caps['browserName'] = ''
desired_caps['version'] = '4.3'
desired_caps['app'] = os.path.join(this_dir,'henrietta-debug.apk')
desired_caps['app-package'] = 'com.rethoughtsolutions.henrietta'
desired_caps['app-activity'] = '.ListProductsActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
try:
	print dir(driver)
	source = driver.page_source
	source = json.loads(source)
	print source
finally:
	driver.quit()