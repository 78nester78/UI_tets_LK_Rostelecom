from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)

    phone = WebElement(id='username')
    password = WebElement(id='password')
    btn_login = WebElement(id='kc-login')
    registration_link = WebElement(id='kc-register')
    lk_navi_bar = WebElement(id='lk-btn')
    invalid_data = WebElement(id='form-error-message')

    auth_text_l = WebElement(xpath='//*[@id="page-left"]/div/div[2]/p')
    logo_left = WebElement(xpath='//*[@id="page-left"]/div/div[1]')
    auth_title_plate = WebElement(xpath='//*[@id="page-right"]/div/div/h1')
    tab_telephone = WebElement(id='t-btn-tab-phone')
    tab_email = WebElement(id='t-btn-tab-mail')
    tab_login = WebElement(id='t-btn-tab-login')
    tab_ls = WebElement(id='t-btn-tab-ls')
    link_agreement = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/a')
    input_elem_mob_phone = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    input_pass_plate = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[2]/div/span[2]')
    input_elem_email = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')

# Поля регистрации
    reg_button = WebElement(id='kc-register')
    name_field = WebElement(name='firstName')
    surname_field = WebElement(name='lastName')
    reg_email_field = WebElement(id='address')
    reg_password_field = WebElement(id='password')
    reg_re_password_field = WebElement(id='password-confirm')
    reg_but = WebElement(name='register')
    pop_up_window = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2')
    invalid_name_plate = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
    invalid_surname_plate = WebElement(xpath='//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')
    region_name_field = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[2]/div/div/span[2]')
    link_agreement_reg = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[5]/a')
    name_field_plate = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/span[2]')
    surname_plate = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    email_field_plate = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[3]/div/span[2]')
    password_field_plate = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/div/span[2]')
    re_password_field_plate = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/div/span[2]')
    reg_but_plate = WebElement(xpath = '//*[@id="page-right"]/div/div/div/form/button')
    plate_password_absence = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')