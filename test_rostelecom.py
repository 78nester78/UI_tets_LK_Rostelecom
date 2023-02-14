import pytest
from pages.auth_locators import AuthPage
from settings import *
from selenium import webdriver


def test_authorization(web_browser):
    """Авторизация пользователя с валидными данными почты и пароля"""
    auth_page = AuthPage(web_browser)
    auth_page.phone.send_keys(valid_email)
    auth_page.password.send_keys(valid_password)
    auth_page.btn_login.click()
    assert auth_page.lk_navi_bar.get_text() == 'Личный кабинет'


def test_auth_with_invalid_password(web_browser):
    """Авторизация пользователя с невалидным паролем"""
    auth_page = AuthPage(web_browser)
    auth_page.phone.send_keys(valid_email)
    auth_page.password.send_keys(invalid_password)
    auth_page.btn_login.click()
    assert auth_page.invalid_data.get_text() == 'Неверный логин или пароль'


def test_auth_with_invalid_email(web_browser):
    """Авторизация пользователя с невалидным значением почты"""
    auth_page = AuthPage(web_browser)
    auth_page.phone.send_keys(invalid_email)
    auth_page.password.send_keys(valid_password)
    auth_page.btn_login.click()
    assert auth_page.invalid_data.get_text() == 'Неверный логин или пароль'


def test_re_registration(web_browser):
    """Пытаемся зарегистрировать уже существующего в системе пользователя"""
    auth_page = AuthPage(web_browser)
    auth_page.reg_button.click()
    auth_page.name_field.send_keys(valid_name)
    auth_page.surname_field.send_keys(valid_surname)
    auth_page.reg_email_field.send_keys(valid_email)
    auth_page.reg_password_field.send_keys(valid_password)
    auth_page.reg_re_password_field.send_keys(valid_password)
    auth_page.reg_but.click()
    assert auth_page.pop_up_window.get_text() == 'Учётная запись уже существует'


@pytest.mark.parametrize("name",
                         ['', 'Ф', 'Abba', 'Фывапротрпнаритсичмсеаролктваир'],
                         ids=["empty", "one letter", "Latin letters", "31 letters"])
def test_reg_with_invalid_name(web_browser, name):
    """Регистрация пользователя с невалидными значениями в поле имени"""
    auth_page = AuthPage(web_browser)
    auth_page.reg_button.click()
    auth_page.name_field.send_keys(name)
    auth_page.surname_field.send_keys(valid_surname)
    auth_page.reg_email_field.send_keys(valid_email)
    auth_page.reg_password_field.send_keys(valid_password)
    auth_page.reg_re_password_field.send_keys(valid_password)
    auth_page.reg_but.click()
    assert auth_page.invalid_name_plate.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@pytest.mark.parametrize("surname",
                         ['', 'Ф', 'Abba', 'Фывапротрпнаритсичмсеаролктваир'],
                         ids=["empty", "one letter", "Latin letters", "31 letters"])
def test_reg_with_invalid_surname(web_browser, surname):
    """Регистрация пользователя с невалидными значениями в поле фамилии"""
    auth_page = AuthPage(web_browser)
    auth_page.reg_button.click()
    auth_page.name_field.send_keys(valid_name)
    auth_page.surname_field.send_keys(surname)
    auth_page.reg_email_field.send_keys(valid_email)
    auth_page.reg_password_field.send_keys(valid_password)
    auth_page.reg_re_password_field.send_keys(valid_password)
    auth_page.reg_but.click()
    assert auth_page.invalid_surname_plate.get_text() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


def test_auth_right_page(web_browser):
    """Проверяем наличие необходимых полей в правой части страницы авторизации"""
    auth_page = AuthPage(web_browser)
    assert auth_page.auth_title_plate.get_text() == 'Авторизация'
    assert auth_page.tab_telephone.is_clickable()
    assert auth_page.tab_email.is_clickable()
    assert auth_page.tab_login.is_clickable()
    assert auth_page.tab_ls.is_clickable()
    assert auth_page.btn_login.is_clickable()
    assert auth_page.link_agreement.is_clickable()
    assert auth_page.reg_button.is_clickable()


def test_auth_left_page(web_browser):
    """Проверяем наличие слогана и логотипа в левой части страницы авторизации"""
    auth_page = AuthPage(web_browser)
    assert auth_page.logo_left.is_presented()
    assert auth_page.auth_text_l.get_text() == 'Персональный помощник в цифровом мире Ростелекома'


@pytest.mark.skip(reason="Наименование Таба выбора аутентификации по номеру не соответствует ТЗ")
def test_phone(web_browser):
    """Проверяем значение кнопки НОМЕР при авторизации по номеру телефона.
    Значение кнопки не совпадает с требованиями ТЗ. Ставим на тест skip и заводим баг репорт"""
    auth_page = AuthPage(web_browser)
    assert auth_page.tab_telephone.get_text() == 'Номер'
    assert auth_page.input_elem_mob_phone.get_text() == 'Номер'
    assert auth_page.input_pass_plate.get_text() == 'Пароль'


@pytest.mark.skip(reason="Наименование формы ввода для почты не соотвествует ТЗ")
def test_email(web_browser):
    """Проверяем значение кнопки ПОЧТА при авторизации по значению электронной почты.
    Значение кнопки не совпадает с требованиями ТЗ. Ставим на тест skip и заводим баг репорт."""
    auth_page = AuthPage(web_browser)
    assert auth_page.tab_email.get_text() == 'Почта'
    auth_page.tab_email.click()
    assert auth_page.input_elem_email.get_text() == 'Почта'
    assert auth_page.input_pass_plate.get_text() == 'Пароль'


def test_right_page_reg(web_browser):
    """Проверяем наличие обязательных полей в правой части страницы регистрации"""
    auth_page = AuthPage(web_browser)
    auth_page.reg_button.click()
    assert auth_page.name_field_plate.get_text() == 'Имя'
    assert auth_page.surname_plate.get_text() == 'Фамилия'
    assert auth_page.region_name_field.get_text() == 'Регион'
    assert auth_page.email_field_plate.get_text() == 'E-mail или мобильный телефон'
    assert auth_page.password_field_plate.get_text() == 'Пароль'
    assert auth_page.re_password_field_plate.get_text() == 'Подтверждение пароля'
    assert auth_page.reg_but.is_clickable()
    assert auth_page.link_agreement_reg.is_clickable()


@pytest.mark.skip(reason="Содержание не соответствует ТЗ")
def test_left_page_reg(web_browser):
    """Проверяем наличие логотипа и слогана в левой части страницы регистрации.
    Так как логотип и слоган отсутствуют ставим на тест skip и заводим баг репорт"""
    auth_page = AuthPage(web_browser)
    auth_page.reg_button.click()
    assert auth_page.logo_left.is_presented()
    assert auth_page.auth_text_l.get_text() == 'Персональный помощник в цифровом мире Ростелекома'


@pytest.mark.skip(reason="Наименование кнопки на странице Регистрация не соотвествует ТЗ")
def test_reg_button(web_browser):
    """Проверяем название кнопки регистрации. Название не совпадает со значением кнопки по ТЗ.
    Ставим на тест skip и заводим баг репорт."""
    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    assert auth_page.reg_but.get_text() == 'Продолжить'


def test_reg_with_empty_re_password(web_browser):
    """Проверяем возможность регистрации пользователя без ввода подтверждения пароля"""
    auth_page = AuthPage(web_browser)
    auth_page.reg_button.click()
    auth_page.name_field.send_keys(valid_name)
    auth_page.surname_field.send_keys(valid_surname)
    auth_page.reg_email_field.send_keys(valid_email)
    auth_page.reg_password_field.send_keys(valid_password)
    auth_page.reg_re_password_field.send_keys('')
    auth_page.reg_but.click()
    assert auth_page.plate_password_absence.get_text() == 'Длина пароля должна быть не менее 8 символов'


def test_reg_with_invalid_re_password(web_browser):
    """Проверяем возможность регистрации пользователя с вводом невалидного подтверждения пароля"""
    auth_page = AuthPage(web_browser)
    auth_page.reg_button.click()
    auth_page.name_field.send_keys(valid_name)
    auth_page.surname_field.send_keys(valid_surname)
    auth_page.reg_email_field.send_keys(valid_email)
    auth_page.reg_password_field.send_keys(valid_password)
    auth_page.reg_re_password_field.send_keys(invalid_password)
    auth_page.reg_but.click()
    assert auth_page.plate_password_absence.get_text() == 'Пароли не совпадают'
