from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data


#1 Вход по кнопке «Войти в аккаунт» на главной
def test_login_via_login_button(registered_user):
    #Регистрация
    driver = registered_user["driver"]
    email = registered_user["email"]
    password = registered_user["password"]

    #Переходим на главную страницу
    driver.get(Data.MAIN_URL)

    #Нажимаем кнопку "Войти аккаунт" 
    driver.find_element(*Locators.MAIN_LOGIN_BUTTON).click()

    #Вводим email и пароль
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу после входа 
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.MAIN_URL))

    #Проверяем по личному кабинету, что вход прошел успешно
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.PROFILE_URL))
    assert driver.current_url == Data.PROFILE_URL


#2 Вход по кнопке «Личный кабинет»
def test_login_via_personal_account(registered_user):
    #Регистрация
    driver = registered_user["driver"]
    email = registered_user["email"]
    password = registered_user["password"]

    #Переходим на главную страницу
    driver.get(Data.MAIN_URL)

    #Нажимаем на "Личный кабинет"
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

    #Вводим email и пароль
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу после входа 
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.MAIN_URL))

    #Проверяем по личному кабинету, что вход прошел успешно
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.PROFILE_URL))
    assert driver.current_url == Data.PROFILE_URL


#3 Вход через кнопку в форме регистрации
def test_login_via_register_link_form(registered_user):
    #Регистрация
    driver = registered_user["driver"]
    email = registered_user["email"]
    password = registered_user["password"]

    #Переходим в форму регистрации
    driver.get(Data.REGISTER_URL)

    #Нажимаем на надпись "Войти" 
    driver.find_element(*Locators.LOGIN_LINK).click()

    #Вводим email и пароль
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу после входа 
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.MAIN_URL))

    #Проверяем по личному кабинету, что вход прошел успешно
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.PROFILE_URL))
    assert driver.current_url == Data.PROFILE_URL

    


#4 Вход по форме Восстановления пароля
def test_login_via_forgott_password_form(registered_user):
    #Регистрация
    driver = registered_user["driver"]
    email = registered_user["email"]
    password = registered_user["password"]

    #Переходим в форму Восстановления пароля
    driver.get(Data.FORGOT_URL)

    #Нажимаем на надпись "Войти" 
    driver.find_element(*Locators.LOGIN_LINK).click()

    #Вводим email и пароль
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу после входа 
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.MAIN_URL))

    #Проверяем по личному кабинету, что вход прошел успешно
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(Data.PROFILE_URL))
    assert driver.current_url == Data.PROFILE_URL