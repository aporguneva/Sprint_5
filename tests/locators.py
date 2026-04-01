from selenium.webdriver.common.by import By

class Locators:
    PERSONAL_ACCOUNT = (By.XPATH, "//a[@href='/account']") #Личный кабинет
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']") #Надпись Зарегистрироваться на странице Входа
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']") #Надпись Восстановить пароль на странице Входа
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']") #Надпись Войти на странице Регистрации и Востановлении пароля
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']") #Надпись Констркутор
    STELLAR_BURGERS_LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a") #логотип

#Поля регистрации
    INPUT_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input") #имя
    INPUT_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") #email
    INPUT_PASSWORD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input") #пароль 

#Кнопки
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка Зарегистрироваться
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") #Кнопка Войти на странице Входа
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт№ на главной странице
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") #Кнопка Выход

#Конструктор 
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']") #Булки
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']") #Соусы
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']") #Начинки

#Разделы конструктора
    CONSTRUCTOR_BUNS = (By.XPATH, "//h2[text()='Булки']")
    CONSTRUCTOR_SAUCES = (By.XPATH, "//h2[text()='Соусы']")
    CONSTRUCTOR_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")



#Ошибка при регситрации
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class,'input__error')]")