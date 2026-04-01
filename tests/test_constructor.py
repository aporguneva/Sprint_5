from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data
import time

#Проверка перехода к разделам конструктора
def test_constructor_sauce(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    wait = WebDriverWait(driver, 3)

    # Клик по вкладке Соусы
    driver.find_element(*Locators.SAUCES_TAB).click()
    assert wait.until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_SAUCES))
    time.sleep(2)

def test_constructor_fillings(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    wait = WebDriverWait(driver, 3)
    # Клик по вкладке Начинки
    driver.find_element(*Locators.FILLINGS_TAB).click()
    assert wait.until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS))
    time.sleep(2)

def test_constructor_buns(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    wait = WebDriverWait(driver, 3)

    # Клик по вкладке начинки
    driver.find_element(*Locators.FILLINGS_TAB).click()
    wait.until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_FILLINGS))
    time.sleep(2)
    # Клик по вкладке Булки
    driver.find_element(*Locators.BUNS_TAB).click()
    assert wait.until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_BUNS))
    time.sleep(2)
