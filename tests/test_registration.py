from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Data
from locators import Locators
from generators import generate_email, generate_password
import time


#Проверка успешной регистрации

def test_successful_registration(registered_user):
    driver = registered_user["driver"]
    email = registered_user["email"]
    password = registered_user["password"]

    #Вход после регистрации
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.MAIN_URL))

    #Проверяем по личному кабинету, что регистрация прошла успешно
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.PROFILE_URL))
    assert driver.current_url == Data.PROFILE_URL

    


#Ошибка при регистрации с некорректным паролем, пароль менее 6 символов
def test_registration_with_short_password(driver):
    email = generate_email()
    password = "12345"  # меньше 6 символов
    name = "TestUser"

    #Открываем главную страницу сайта
    driver.get(Data.MAIN_URL)

    #Переходим к регистрации
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.REGISTER_LINK).click()

    #Заполняем форму регистрации
    driver.find_element(*Locators.INPUT_NAME).send_keys(name)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)

    #Нажимаем кнопку Зарегистрироваться
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    #Ждем ошибку
    WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located(Locators.ERROR_MESSAGE)
)

    #Проверка ошибки
    error = driver.find_element(*Locators.ERROR_MESSAGE)
    assert error.is_displayed()
    assert error.text == Data.INCORRECT_PASSWORD_TEXT

    time.sleep(3)


   
    

    