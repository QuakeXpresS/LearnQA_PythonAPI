import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
first_response = response.history[0]
second_response = response.history[1]
third_response = response.history[2]

print("Первый редирект: "+first_response.url)
print("Второй редирект: "+second_response.url)
print("Третий редирект: "+third_response.url)
print("Конечный URL: "+third_response.url)
print("Число редиректов: 3")
