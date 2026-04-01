import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators
from generators import generate_email, generate_password

# Фикстура для инициализации и закрытия браузера
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Фикстура регистрации пользователя
@pytest.fixture(scope="function")
def registered_user(driver):
    email = generate_email()
    password = generate_password()
    name = "TestUser"

    #Открываем главную страницу
    driver.get(Data.MAIN_URL)

    #Нажимаем на личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

    #Нажимаем на надпись Зарегистрироваться
    driver.find_element(*Locators.REGISTER_LINK).click()

    # Заполняем поля регистрации
    driver.find_element(*Locators.INPUT_NAME).send_keys(name)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)

    #Нажимаем кнопку зарегистрироваться
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Ожидаем загрзки страницы Входа
    WebDriverWait(driver, 3).until(EC.url_to_be(Data.LOGIN_URL))

    return {
        "email": email,
        "password": password,
        "driver": driver
    }



    