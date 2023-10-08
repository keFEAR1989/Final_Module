import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Тест для сценария с корректными данными
def test_correct_phone_authentication(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    phone_input = browser.find_element_by_id("phone_input")
    phone_input.send_keys("1234567890")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    # Дождитесь отправки кода и перехода на следующую страницу
    sleep(3)  # Предположим, что требуется немного времени на отправку кода
    
    # Проверка, что перенаправление произошло корректно
    assert browser.current_url == "https://example.com/redirect_uri"

# Аналогичный тест для авторизации по почте
def test_correct_email_authentication(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    email_input = browser.find_element_by_id("email_input")
    email_input.send_keys("test@example.com")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    sleep(3)
    
    assert browser.current_url == "https://example.com/redirect_uri"

# Тест ввода некорректных данных
def test_incorrect_phone_input(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    phone_input = browser.find_element_by_id("phone_input")
    phone_input.send_keys("123")  # Некорректный номер
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    # Проверка вывода ошибки о некорректном номере
    assert "Invalid phone number" in browser.page_source

# Аналогичный тест для некорректной почты
def test_incorrect_email_input(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    email_input = browser.find_element_by_id("email_input")
    email_input.send_keys("invalid-email")  # Некорректная почта
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    assert "Invalid email address" in browser.page_source

# Тест для блокировки после некорректных попыток ввода
def test_lockout_after_incorrect_attempts(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    phone_input = browser.find_element_by_id("phone_input")
    phone_input.send_keys("1234567890")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    for _ in range(4):
        code_input = browser.find_element_by_id("code_input")
        code_input.send_keys("111111")
        code_input.send_keys(Keys.ENTER)
    
    assert "Account locked" in browser.page_source

# Аналогичные тесты для других сценариев

# Тесты для изменения номера/почты после получения кода
def test_change_phone_after_getting_code(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    phone_input = browser.find_element_by_id("phone_input")
    phone_input.send_keys("1234567890")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    change_phone_link = browser.find_element_by_id("change_phone_link")
    change_phone_link.click()
    
    new_phone_input = browser.find_element_by_id("new_phone_input")
    new_phone_input.send_keys("9876543210")
    get_code_button.click()
    
    assert "New code sent" in browser.page_source
    
    code_input = browser.find_element_by_id("code_input")
    code_input.send_keys("111111")
    code_input.send_keys(Keys.ENTER)
    
    assert "Successfully changed phone" in browser.page_source

# Аналогичные тесты для изменения почты
def test_change_email_after_getting_code(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    email_input = browser.find_element_by_id("email_input")
    email_input.send_keys("test@example.com")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    change_email_link = browser.find_element_by_id("change_email_link")
    change_email_link.click()
    
    new_email_input = browser.find_element_by_id("new_email_input")
    new_email_input.send_keys("new@example.com")
    get_code_button.click()
    
    assert "New code sent" in browser.page_source
    
    code_input = browser.find_element_by_id("code_input")
    code_input.send_keys("111111")
    code_input.send_keys(Keys.ENTER)
    
    assert "Successfully changed email" in browser.page_source

# Тест для повторной отправки кода после истечения времени
def test_resend_code_after_timeout(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    phone_input = browser.find_element_by_id("phone_input")
    phone_input.send_keys("1234567890")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    sleep(61)  # Дождитесь истечения времени
    
    resend_code_link = browser.find_element_by_id("resend_code_link")
    resend_code_link.click()
    
    assert "New code sent" in browser.page_source


#Тест для успешной смены номера/почты и негативной авторизации:
def test_change_password_after_authentication(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    phone_input = browser.find_element_by_id("phone_input")
    phone_input.send_keys("1234567890")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    # Предположим, что успешная авторизация произошла здесь
    sleep(3)
    
    change_password_link = browser.find_element_by_id("change_password_link")
    change_password_link.click()
    
    new_password_input = browser.find_element_by_id("new_password_input")
    new_password_input.send_keys("new_password123")
    confirm_password_input = browser.find_element_by_id("confirm_password_input")
    confirm_password_input.send_keys("new_password123")
    change_password_button = browser.find_element_by_id("change_password_button")
    change_password_button.click()
    
    assert "Password changed successfully" in browser.page_source

#Тест для успешной смены пароля после авторизации:
def test_change_password_with_mismatched_passwords(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    phone_input = browser.find_element_by_id("phone_input")
    phone_input.send_keys("1234567890")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    sleep(3)
    
    change_password_link = browser.find_element_by_id("change_password_link")
    change_password_link.click()
    
    new_password_input = browser.find_element_by_id("new_password_input")
    new_password_input.send_keys("new_password123")
    confirm_password_input = browser.find_element_by_id("confirm_password_input")
    confirm_password_input.send_keys("different_password")
    change_password_button = browser.find_element_by_id("change_password_button")
    change_password_button.click()
    
    assert "Passwords do not match" in browser.page_source

#Тест для неверной смены пароля (разные пароли):
def test_logout(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    
    # Предположим, что произошла успешная авторизация
    sleep(3)
    
    logout_link = browser.find_element_by_id("logout_link")
    logout_link.click()
    
    assert "Logged out successfully" in browser.page_source

#Тест для успешной выхода из аккаунта:
def test_negative_auth_with_invalid_code(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    phone_input = browser.find_element_by_id("phone_input")
    phone_input.send_keys("1234567890")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    sleep(3)
    
    code_input = browser.find_element_by_id("code_input")
    code_input.send_keys("000000")  # Недействительный код
    code_input.send_keys(Keys.ENTER)
    
    assert "Invalid code" in browser.page_source

#Тест для негативной авторизации с недействительным кодом:
def test_negative_auth_with_invalid_credentials(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    phone_input = browser.find_element_by_id("phone_input")
    phone_input.send_keys("invalid_phone")
    get_code_button = browser.find_element_by_id("get_code_button")
    get_code_button.click()
    
    sleep(3)
    
    assert "Invalid credentials" in browser.page_source

#Тест для негативной авторизации с неверными учетными данными:
def test_forgot_password_and_reset_password(browser):
    browser.get("https://lk.smarthome.rt.ru/")
    
    forgot_password_link = browser.find_element_by_id("forgot_password_link")
    forgot_password_link.click()
    
    # Предположим, что здесь пользователь вводит свой номер/почту и отправляет запрос на сброс пароля
    
    assert "Password reset instructions sent" in browser.page_source
