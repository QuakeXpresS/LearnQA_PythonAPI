import requests


url = "https://playground.learnqa.ru/api/homework_cookie"

response = requests.get(url=url)

cookie = response.cookies.get_dict()
print("Куки полученные с сайта:", cookie)
cookie_value = cookie['HomeWork']
print("Значение куки:", cookie_value)

assert cookie == response.cookies.get_dict()
assert cookie_value == response.cookies.get_dict()['HomeWork'], f"Значение куки не совпадает"

