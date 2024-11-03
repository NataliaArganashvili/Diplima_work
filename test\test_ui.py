from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome()

from pages_aviasales.main_page import MainPage

#Проверка в одну сторону
def test_one_way():
    main_page = MainPage(driver)
    main_page.fill_origin("Москва")
    main_page.fill_destination("Новокузнецк")
    main_page.open_calender()
    main_page.choose_date("12.12.2024")
    main_page.click_search()
    main_page.waiter()
    origin = main_page.get_origin_value()
    destination = main_page.get_destination_value()
    driver.quit()
    assert origin == "Москва" 
    assert destination == "Новокузнецк"

#Проверка туда и обратно
def test_two_ways():
    main_page = MainPage(driver)
    main_page.fill_origin("Москва")
    main_page.fill_destination("Новокузнецк")
    main_page.open_calender()
    main_page.choose_date("12.12.2024")
    main_page.choose_date("19.12.2024")
    main_page.click_search()
    main_page.waiter()
    origin = main_page.get_origin_value()
    destination = main_page.get_destination_value()
    driver.quit()
    assert origin == "Москва" 
    assert destination == "Новокузнецк"

#Проверка 2 пассажиров
def test_two_passangers():
    main_page = MainPage(driver)
    main_page.fill_origin("Москва")
    main_page.fill_destination("Новокузнецк")
    main_page.open_calender()
    main_page.choose_date("12.12.2024")
    main_page.choose_passangers_quantity()
    main_page.click_search()
    main_page.waiter()
    passengers_quantity = main_page.get_passengers_quantity()
    driver.quit()
    assert "2 пассажира" in passengers_quantity

#Проверка первого-класса
def test_first_class():
    main_page = MainPage(driver)
    main_page.fill_origin("Москва")
    main_page.fill_destination("Новокузнецк")
    main_page.open_calender()
    main_page.choose_date("12.12.2024")
    main_page.choose_first_class()
    main_page.click_search()
    main_page.waiter()
    class_name = main_page.get_class()
    driver.quit()
    assert "Первый класс" in class_name
    
#Проверка класса комфорт
def test_comfort_class():
    main_page = MainPage(driver)
    main_page.fill_origin("Москва")
    main_page.fill_destination("Новокузнецк")
    main_page.open_calender()
    main_page.choose_date("12.12.2024")
    main_page.choose_comfort_class()
    main_page.click_search()
    main_page.waiter()
    class_name = main_page.get_class()
    driver.quit()
    assert "Комфорт" in class_name
    
