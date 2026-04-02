from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *
from locators import Locators
from generators import generate_email, generate_password



#Проверка успешной регистрации

def test_successful_registration(driver):
    name = Data.TEST_USER_NAME
    email = generate_email()
    password = generate_password()

    # Открываем главную страницу
    driver.get(URL.MAIN_URL)

    # Переходим в личный кабинет
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.PERSONAL_ACCOUNT)
    ).click()

    # Переходим на страницу регистрации
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.REGISTER_LINK)
    ).click()

    # Заполняем форму регистрации
    driver.find_element(*Locators.INPUT_NAME).send_keys(name)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)

    # Нажимаем кнопку "Зарегистрироваться"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    ).click()

    # Ожидаем перехода на страницу входа
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.LOGIN_URL))

    #Вход после регистрации
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.MAIN_URL))

    #Переходим в личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    
    #Проверяем по личному кабинету, что регистрация прошла успешно
    assert WebDriverWait(driver, 5).until(EC.url_to_be(URL.PROFILE_URL))

    


#Ошибка при регистрации с некорректным паролем, пароль менее 6 символов
def test_registration_with_short_password(driver):
    email = generate_email()
    password = Data.SHORT_PASSWORD  
    name = Data.TEST_USER_NAME 

    #Открываем главную страницу сайта
    driver.get(URL.MAIN_URL)

    #Переходим к регистрации
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.REGISTER_LINK).click()

    #Заполняем форму регистрации
    driver.find_element(*Locators.INPUT_NAME).send_keys(name)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)

    #Нажимаем кнопку Зарегистрироваться
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    #Проверка ошибки при некорректном пароле
    assert WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(
            Locators.ERROR_MESSAGE)).text == Data.INCORRECT_PASSWORD_TEXT

    


   
    

    