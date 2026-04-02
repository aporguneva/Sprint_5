#Ссылки на страницы сайта
class URL:
    #Адрес сервера
    BASE_URL = "https://stellarburgers.education-services.ru"
    # Эндпоинты
    MAIN_URL = f"{BASE_URL}/" #Главная страница
    LOGIN_URL = f"{BASE_URL}/login" #Страница входа
    REGISTER_URL = f"{BASE_URL}/register" #Страница регистрации
    FORGOT_PASSWORD_URL = f"{BASE_URL}/forgot-password" #Страница восстановления пароля
    PROFILE_URL = f"{BASE_URL}/account/profile" #Личный кабинет профиля

#Тестовые данные 
class Data:
    #Текст ошибки при регистрации
    INCORRECT_PASSWORD_TEXT = "Некорректный пароль"
    # Данные для тестового пользователя
    TEST_USER_NAME = "TestUser" #Имя
    SHORT_PASSWORD = "12345" #Пароль менее 6 символов