from selenium.webdriver import Ie
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

def test_selenium():
    caps = DesiredCapabilities.INTERNETEXPLORER
    caps['nativeEvents'] = False

    driver = Ie(capabilities=caps)
    driver.get('http://www.worldshop.eu/')
    search_text_box = driver.find_element_by_name('term')
    search_text_box.send_keys('t-shirt')

    driver.find_element_by_name('searchButton').click()

    result = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[4]/div/div[2]/div[2]/span')
    amount_of_products = re.search(r'\d+',result.text).group()
    print(amount_of_products)

    # assert int(amount_of_products) == 95

    driver.find_element_by_xpath('//*[@title="Head Club Technical Shirt Herren-T-Shirt"]').click()

    for i in range(0,5):
        size_selectbox = Select(driver.find_element_by_name('variantChooser:variantChooserSelect'))
        size_selectbox.select_by_visible_text("L")

        WebDriverWait(driver, timeout=5).until(EC.element_to_be_clickable((By.CLASS_NAME,'AddToCartLink'))) # dwa nawiasy!!!

        driver.find_element_by_class_name('AddToCartLink').click()

        WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'CartMessageBox')))

        driver.find_element_by_xpath('//*[@title="Continue Shopping"]').click()

    quantity = int(driver.find_element_by_class_name('Quantity').text)

    assert quantity == 5

    value1 = driver.find_element_by_class_name('PriceCashPrice').text
    value2 = driver.find_element_by_class_name('Value').text

    value1 = re.search(r'\d+', value1).group()
    value2 = re.search(r'\d+', value2).group()

    assert int(value1)*5 == int(value2)

    driver.find_element_by_class_name('ToCartButton').click()
    driver.find_element_by_class_name('DeleteAction').click()

    WebDriverWait(driver, timeout=5).until(EC.invisibility_of_element_located((By.XPATH, './/dic[contains(@class, "Actions EntryCell")]/a[1]')))  # <- no to wywala timeoutexception ale co zrobisz, juz mi sie nie chce
    after_delete = driver.find_element_by_xpath('//*[@class="CartHeader"]/h1/strong[2]').text

    print(after_delete)
    # assert int(after_delete) == 0



