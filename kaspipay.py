import unittest
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

# Конфигурация для Каспи
capabilities = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "deviceName": "Redmi Note 10 Pro",
    "appPackage": "hr.asseco.android.kaspibusiness",  # Пакет Kaspi Pay
    "appActivity": "kz.kaspibusiness.view.ui.main.BusinessActivity",  # Правильная активность
    "noReset": True,  # Чтобы приложение не перезапускалось заново
    "autoGrantPermissions": True  # Автоматически выдавать разрешения
}

appium_server_url = 'http://localhost:4723'

class TestKaspiPay(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_kaspi_pay_connection(self):
        # Активируем приложение Kaspi Pay
        self.driver.activate_app('hr.asseco.android.kaspibusiness')

        # Ждем, пока нужная активность станет активной
        self.driver.wait_activity('kz.kaspibusiness.view.ui.main.BusinessActivity', timeout=10)

        # Ждем, пока кнопка станет доступной для нажатия
        self.driver.implicitly_wait(10)  # Подождите до 10 секунд

        # Находим кнопку "Подключиться" и нажимаем на неё
        self.driver.find_element(by=AppiumBy.ID, value='hr.asseco.android.kaspibusiness:id/floatingBtn').click()

        # Дополнительные проверки или действия после нажатия кнопки

        # Ждем, пока поле ввода номера телефона станет доступным
        sleep(2)  # Можно использовать WebDriverWait для более надежного ожидания

        phone_input = self.driver.find_element(by=AppiumBy.ID,
                                               value='hr.asseco.android.kaspibusiness:id/editPhoneNumber')
        phone_input.click()
        phone_input.clear()

        # Вводим номер телефона
        phone_number = '+7(123)456-78-90'  # Укажите нужный номер телефона
        phone_input.send_keys(phone_number)

        # Нажимаем кнопку "Продолжить"
        continue_button = self.driver.find_element(by=AppiumBy.ID,
                                                   value='hr.asseco.android.kaspibusiness:id/btn_continue')
        continue_button.click()



if __name__ == '__main__':
    unittest.main()
