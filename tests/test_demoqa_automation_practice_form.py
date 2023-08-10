import allure
from allure_commons.types import Severity

from qa_guru_6_10.pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "lysenko")
@allure.feature("Проверка web-формы регистрации")
@allure.story("test_steps")
def test_hard(browser_size):
    # fill form
    registration_page = RegistrationPage()
    with allure.step('Открываем форму регистрации'):
        registration_page.open_browser()

    with allure.step('Заполняем форму регистрации'):
        registration_page.fill_first_name('Alex')
        registration_page.fill_second_name('Lys')
        registration_page.fill_email('example@yandex.ru')
        registration_page.choise_gender('Male')
        registration_page.fill_phone_number('1234567890')
        registration_page.fill_date_of_birth('1992', 'January', '05')
        registration_page.choise_subjects('economics')
        registration_page.choise_hobbies('Sports')
        registration_page.upload_photo('Skrik.jpg')
        registration_page.fill_address('godovikova 9')
        registration_page.choise_state('NCR')
        registration_page.choise_city('Delhi')
        registration_page.submit()

    # check form
    with allure.step('Проверяем форму регистрации'):
        registration_page.should_registered_user_with('Alex Lys', 'example@yandex.ru', 'Male', '1234567890',
                                                      '05 January,1992', 'Economics', 'Sports', 'Skrik.jpg',
                                                      'godovikova 9',
                                                      'NCR Delhi')
