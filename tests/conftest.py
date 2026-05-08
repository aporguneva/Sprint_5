import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data import Data, URL
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
    name = Data.TEST_USER_NAME 

    #Открываем главную страницу
    driver.get(URL.MAIN_URL)

    #Нажимаем на личный кабинет
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
    ).click()

    #Нажимаем на надпись Зарегистрироваться
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.REGISTER_LINK)
    ).click()

    # Заполняем поля регистрации
    driver.find_element(*Locators.INPUT_NAME).send_keys(name)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)

    #Нажимаем кнопку зарегистрироваться
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    ).click()

    # Ожидаем загрзки страницы Входа
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.LOGIN_URL))

    return {
        "email": email,
        "password": password,
        "driver": driver
    }



    