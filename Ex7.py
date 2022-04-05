import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

# Первый вопрос
response = requests.get(url=url)
print("Первый вопрос: ", response.text)

# Второй вопрос
response = requests.head(url=url)
print("Второй вопрос: ", response.text)


# Третий вопрос
method_get = {
    "method": "GET"
}
response = requests.get(url=url, params=method_get)
print("Третий вопрос: ", response.text)

# Четвертый вопрос

methods_all = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']
i = 0

while i <= 4:
    payload = {'method': methods_all[i]}
    response = requests.get(url=url, params=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i], "Код ответа "
                                                                                                         "сервера: ",
          response.status_code, "Текст ответа: ", response.text)
    i = i+1

i = 0

while i <= 4:
    payload = {'method': methods_all[i]}
    response = requests.post(url=url, data=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i], "Код ответа "
                                                                                                         "сервера: ",
          response.status_code, "Текст ответа: ", response.text)
    i = i+1

i = 0

while i <= 4:
    payload = {'method': methods_all[i]}
    response = requests.put(url=url, data=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i], "Код ответа "
                                                                                                         "сервера: ",
          response.status_code, "Текст ответа: ", response.text)
    i = i+1

i = 0

while i <= 4:
    payload = {'method': methods_all[i]}
    response = requests.delete(url=url, data=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i], "Код ответа "
                                                                                                         "сервера: ",
          response.status_code, "Текст ответа: ", response.text)
    i = i+1

i = 0

while i <= 4:
    payload = {'method': methods_all[i]}
    response = requests.head(url=url, data=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i], "Код ответа "
                                                                                                         "сервера: ",
          response.status_code, "Текст ответа: ", response.text)
    i = i+1

i = 0
