from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data


#Выход из профиля

def test_logout(registered_user):
    driver = registered_user["driver"]
    email = registered_user["email"]
    password = registered_user["password"]

    #Вход после регистрации
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.MAIN_URL))

    #Кликаем  на личный кабинет 
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.PROFILE_URL))

    #Кликаем на выход и ожидаем переход на страницу входа
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.LOGIN_URL))
    assert driver.current_url == Data.LOGIN_URL