from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import URL


#Переход в личный кабинет
def test_navigate_personal_account(registered_user):
    driver = registered_user["driver"]
    email = registered_user["email"]
    password = registered_user["password"]

    #Вход после регистрации
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.MAIN_URL))

    #Кликаем  на личный кабинет и проверяем переход
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    assert WebDriverWait(driver, 5).until(EC.url_to_be(URL.PROFILE_URL))

#Переход из личного кабинета в конструктор по клику на "Конструктор"
    
def test_navigate_from_personal_account_to_constuctor(registered_user):
    driver = registered_user["driver"]
    email = registered_user["email"]
    password = registered_user["password"]

    #Вход после регистрации
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.MAIN_URL))

    #Кликаем  на личный кабинет и ожидаем переход
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.PROFILE_URL))

    #Кликаем на конструктор и проверяем переход из личного кабинета в конструктор

    driver.find_element(*Locators.CONSTRUCTOR_LINK).click()
    assert WebDriverWait(driver, 5).until(EC.url_to_be(URL.MAIN_URL))
    

#Переход из личного кабинета в конструктор по клику на логотип Stella Burgers
    
def test_navigate_from_personal_account_logo(registered_user):
    driver = registered_user["driver"]
    email = registered_user["email"]
    password = registered_user["password"]

    #Вход после регистрации
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    #Ждем переход на главную страницу
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.MAIN_URL))

    #Кликаем  на личный кабинет и ожидаем переход
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(URL.PROFILE_URL))

    #Кликаем на логотип и проверяем переход из личного кабинета в конструктор
    driver.find_element(*Locators.STELLAR_BURGERS_LOGO).click()
    assert WebDriverWait(driver, 5).until(EC.url_to_be(URL.MAIN_URL))
    
 

