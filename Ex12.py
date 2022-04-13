import requests


url = "https://playground.learnqa.ru/api/homework_header"

response = requests.get(url=url)

header = response.headers
print("заголовки полученные с сайта:", header)

header_date = response.headers['Date']
header_content_type = response.headers['Content-Type']
header_content_lenght = response.headers['Content-Length']
header_connection = response.headers['Connection']
header_keep_alive = response.headers['Keep-Alive']
header_server = response.headers['Server']
header_secret_homework = response.headers['x-secret-homework-header']
header_cache_control = response.headers['Cache-Control']
header_expires = response.headers['Expires']

print("Значение искомого заголовка:", header_secret_homework)

if header_secret_homework is None:
    f"Отсутствует значение в заголовке x-secret-homework-header"
else:
    assert header_secret_homework == "Some secret value", f"Значение в заголовке " \
                                                      f"'x-secret-homework-header' не соответствует"
