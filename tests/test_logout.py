from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import URL


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
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.MAIN_URL))

    #Кликаем  на личный кабинет 
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.PROFILE_URL))

    #Кликаем на выход
    driver.find_element(*Locators.LOGOUT_BUTTON).click()
    #Проверяем переход на страницу входа
    assert WebDriverWait(driver, 5).until(EC.url_to_be(URL.LOGIN_URL))
    