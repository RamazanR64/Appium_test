import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

# Конфигурация для калькулятора MIUI
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Redmi Note 10 Pro',
    appPackage='com.miui.calculator',  # Пакет MIUI Калькулятора
    appActivity='.cal.CalculatorActivity',  # Правильная активность
    noReset=True,  # Чтобы приложение не перезапускалось заново
    autoGrantPermissions=True  # Автоматически выдавать разрешения
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        # Создаем соединение с Appium сервером с использованием указанных capabilities
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def tearDown(self) -> None:
        # Закрываем сессию драйвера, если она существует
        if self.driver:
            self.driver.quit()

    def test_calculator_addition(self) -> None:
        # Пример: 2 + 3 = 5
        try:
            self.driver.find_element(by=AppiumBy.ID, value='com.miui.calculator:id/btn_2_s').click()
            self.driver.find_element(by=AppiumBy.ID, value='com.miui.calculator:id/btn_plus_s').click()
            self.driver.find_element(by=AppiumBy.ID, value='com.miui.calculator:id/btn_3_s').click()
            self.driver.find_element(by=AppiumBy.ID, value='com.miui.calculator:id/btn_equal_s').click()

            # Получаем результат и проверяем его
            result = self.driver.find_element(by=AppiumBy.ID, value='com.miui.calculator:id/result').text
            print(f"Result: {result}")
            self.assertEqual(result, '5')
        except NoSuchElementException as e:
            print(f"Element not found: {e}")

if __name__ == '__main__':
    unittest.main()
