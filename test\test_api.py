import requests

@allure.title("Проверка сайта aviasales.ru поиска авиабилетов")
@allure.description("Проверка сайта поиска авиабилетов")
@allure.feature("GET") 
@allure.severity("blocker")

base_url = "https://min-prices.aviasales.ru/price_matrix?"

my_headers = {
    "Content-Type": "application/json"
}

def test_get_oneway_positive() -> str:
    """Поиск билета в одну сторону - позитивная проверка"""
    city1 = "MOW"
    city2 = "STW"
    date = "2024-12-15"
    with allure.step("Получение списка билетов в одну сторону"):
        tickets_list = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    lst = tickets_list.json()
    with allure.step("Проверка"):
        assert len(lst) > 0

def test_get_twoways_positive() -> str:
    """Поиск билета в обе стороны - позитивная проверка"""
    city1 = "MOW"
    city2 = "STW"
    date1 = "2024-12-15"
    date2 = "2024-12-25"
    with allure.step("Получение списка билетов в обе стороны"):
        tickets_list = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date1}&return_start={date2}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    lst = tickets_list.json()
    with allure.step("Проверка"):
        assert len(lst) > 0

def test_get_date_31_positive() -> str:
    """Поиск билета с числом 31 месяца с 31 днями - позитивная проверка"""
    city1 = "MOW"
    city2 = "STW"
    date1 = "2024-12-15"
    date2 = "2024-12-31"
    with allure.step("Получение списка билетов на дату 31 месяца с 31 днями"):
        tickets_list = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date1}&return_start={date2}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    lst = tickets_list.json()
    with allure.step("Проверка"):
        assert len(lst) > 0

def test_get_date_31_negative() -> str:
    """Поиск билета с числом 31 месяца с 30 днями - негативная проверка"""
    city1 = "MOW"
    city2 = "NOZ"
    date = "2024-11-31"
    with allure.step("Проверка даты 31 для месяца с 30 днями"):
        resp = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    with allure.step("Проверка"):
        assert resp.status_code == 400

def test_get_invalid_city_code() -> str:
    """Поиск билета в город с невалидным кодом - негативная проверка"""
    city1 = "MOW"
    city2 = "QWE"
    date = "2024-11-30"
    with allure.step("Проверка невалидного кода города"):
        resp = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    with allure.step("Проверка"):
        assert resp.status_code == 400
