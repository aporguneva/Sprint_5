from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import URL

#Проверка перехода к разделам конструктора
def test_constructor_sauce(driver):
    driver.get(URL.MAIN_URL)

    # Клик по вкладке Соусы
    driver.find_element(*Locators.SAUCES_TAB).click()
    assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.SAUCES_TAB_ACTIVE))

def test_constructor_fillings(driver):
    driver.get(URL.MAIN_URL)
    # Клик по вкладке Начинки
    driver.find_element(*Locators.FILLINGS_TAB).click()
    assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FILLINGS_TAB_ACTIVE))


def test_constructor_buns(driver):
    driver.get(URL.MAIN_URL)

    # Клик по вкладке начинки
    driver.find_element(*Locators.FILLINGS_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.FILLINGS_TAB_ACTIVE))
 
    # Клик по вкладке Булки
    driver.find_element(*Locators.BUNS_TAB).click()
    assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.BUNS_TAB_ACTIVE))
