from selenium.webdriver import Ie
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_selenium():
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['nativeEvents'] = False

    driver = Ie(capabilities=caps)
    driver.get('http://www.worldshop.eu/')
    search_text_box = driver.find_element_by_name('term')
    search_text_box.send_keys('t-shirt')

    driver.find_element_by_name('searchButton').click()


test_selenium()
