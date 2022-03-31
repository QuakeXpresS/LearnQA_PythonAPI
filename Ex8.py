import time
import requests

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)

parsed_response_text = response.json()

timer = parsed_response_text["seconds"]
token = parsed_response_text["token"]

# URL, на который собираетесь отправлять запрос
url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

params = {
    "token": token,
}

# Запрос без задержки
response = requests.get(url=url, params=params)
print(response.text)
parsed_response_text = response.json()
status = parsed_response_text["status"]

if status == "Job is NOT ready":
    print("Поле статус соответствует: Работа не готова")
else:
    print("Поле статус не соответствует: Почему то выдал что готова")

# запрос с задержкой (timer)
time.sleep(timer)
response = requests.get(url=url, params=params)
print(response.text)

parsed_response_text = response.json()
status = parsed_response_text["status"]
result = parsed_response_text["result"]

if status == "Job is ready":
    print("Поле статус соответствует: Работа выполнена")
else:
    print("Поле статус не соответствует: Почему то выдал что не готова")

if result is not None:
    print("Поле с результатом присутствует")
else:
    print("Поле с результатом отсутствует")
