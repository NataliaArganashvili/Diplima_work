from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

from pages_aviasales.main_page import MainPage

@allure.title("Проверка открытия страницы aviasales.ru и автоматическое заполнение города")
@allure.severity("medium")
def test_open_page():
    current_city = "Москва"
    main_page = MainPage(driver)
    assert driver.find_element(By.ID, "avia_form_origin-input").get_attribute("value") == current_city
    driver.quit()

@allure.title("Проверка того, что открывается страница https://ostrovok.ru/ при поиске билетов")
@allure.severity("medium")
def test_hotels():
    main_page = MainPage(driver)
    main_page.fill_origin("Москва")
    main_page.fill_destination("Новокузнецк")
    main_page.open_calender()
    main_page.choose_date("12.12.2024")
    main_page.click_search()
    assert "https://ostrovok.ru/" in driver.current_url

@allure.title("Проверка загаловка страницы")
@allure.severity("medium")
def test_text():
    driver.get("https://www.aviasales.ru/")
    expected_text = "Тут покупают дешёвые авиабилеты"
    header = driver.find_element(By.CSS_SELECTOR, "h1.header__title")
    assert header.text == expected_text

@allure.title("Негативный тест на проверку заполнения без города")
@allure.severity("critical")
def test_negative_destination():
    main_page = MainPage(driver)
    main_page.click_search()
    element = driver.find_element(By.XPATH, '//div[text()="Укажите город прибытия"]')
    assert element.is_displayed()

@allure.title("Негативный тест на проверку заполнения без даты")
@allure.severity("critical")
def test_negative_date():
    main_page = MainPage(driver)
    main_page.click_search()
    element = driver.find_element(By.XPATH, '//div[text()="Укажите дату"]')
    assert element.is_displayed()
