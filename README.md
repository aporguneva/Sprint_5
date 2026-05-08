# Sprint_5
Файл url.py содержит адреса страниц
Файл data.py содержит данные для тестирования и ссылки на страницы сайта
Файл generators.py содержит генераторы почты и пароля
Файл locators.py содержит локторы

Файл test_registration.py:

test_successful_registration(registered_user) - проверяет успешную регистрацию
test_registration_with_short_password(driver) - проверяет ошибку при некоррктном пароле

Файл test_login.py:

test_login_via_login_button(registered_user) - проверяет вход по кнопке «Войти в аккаунт» на главной
test_login_via_personal_account(registered_user) - проверяет вход по кнопке «Личный кабинет»
test_login_via_register_link_form(registered_user) - проверяет вход через кнопку Войти в форме регистрации
test_login_via_forgott_password_form(registered_user) - проверяет вход через кнопку Войти в форме Восстановления пароля

Файл test_navigate.py:

test_navigate_personal_account(registered_user) проверяет переход в личный кабинет
test_navigate_from_personal_account_to_constuctor(registered_user) -проверяет переход из личного кабинета в конструктор по клику на "Конструктор"
test_navigate_from_personal_account_logo(registered_user)- проверяет переход из личного кабинета по клику на логотип Stella Burgers

Файл test_logout:

test_logout(registered_user) - проверяет выход из профиля

Файл test_constructor.py:

test_constructor_sauce(driver) - проверяет переход к разделу Соусы
test_constructor_fillings(driver) -проверяет переход к разделу Начинки
test_constructor_buns(driver) - проверяет переход к разделу Булки
