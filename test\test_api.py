import requests

base_url = "https://min-prices.aviasales.ru/price_matrix?"

my_headers = {
    "Content-Type": "application/json"
}

def test_get_oneway_positive() -> str:
    """Поиск билета в одну сторону - позитивная проверка"""
    city1 = "MOW"
    city2 = "STW"
    date = "2024-12-15"
    tickets_list = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    lst = tickets_list.json()
    assert len(lst) > 0

def test_get_twoways_positive() -> str:
    """Поиск билета в обе стороны - позитивная проверка"""
    city1 = "MOW"
    city2 = "STW"
    date1 = "2024-12-15"
    date2 = "2024-12-25"
    tickets_list = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date1}&return_start={date2}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    lst = tickets_list.json()
    assert len(lst) > 0

def test_get_date_31_positive() -> str:
    """Поиск билета с числом 31 месяца с 31 днями - позитивная проверка"""
    city1 = "MOW"
    city2 = "STW"
    date1 = "2024-12-15"
    date2 = "2024-12-31"
    tickets_list = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date1}&return_start={date2}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    lst = tickets_list.json()
    assert len(lst) > 0

def test_get_date_31_negative() -> str:
    """Поиск билета с числом 31 месяца с 30 днями - негативная проверка"""
    city1 = "MOW"
    city2 = "NOZ"
    date = "2024-11-31"
    resp = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    assert resp.status_code == 400

def test_get_invalid_city_code() -> str:
    """Поиск билета в город с невалидным кодом - негативная проверка"""
    city1 = "MOW"
    city2 = "QWE"
    date = "2024-11-30"
    resp = requests.get(base_url + f'origin_iata={city1}&destination_iata={city2}&depart_start={date}&depart_range=6&return_range=6&affiliate=false&market=ru', headers=my_headers) 
    assert resp.status_code == 400
