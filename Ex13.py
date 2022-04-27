import requests
import json


user_agents = ['Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, '
               'like Gecko) Version/4.0 Mobile Safari/534.30', 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) '
                                                               'AppleWebKit/605.1.15 (KHTML, like Gecko) '
                                                               'CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
               'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
               'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) '
               'Version/13.0.3 Mobile/15E148 Safari/604.1']

platforms = ['Mobile', 'Mobile', 'Googlebot', 'Web', 'Mobile']
browsers = ['No', 'Chrome', 'Unknown', 'Chrome', 'No']
devices = ['Android', 'iOS', 'Unknown', 'No', 'iPhone']

i = 0

while i <= 4:
    response = requests.get(
        "https://playground.learnqa.ru/ajax/api/user_agent_check",
        headers={"User-Agent": user_agents[i]}
    )

    json_text = response.text
    response_dict = json.loads(json_text)
    v_platform = response_dict['platform']
    v_browser = response_dict['browser']
    v_device = response_dict['device']

    if platforms[i] != v_platform:
        print("Значение платформы не соответствует, требовалось:", platforms[i], "а получено в ответ", v_platform,
              "неверный UserAgent:", user_agents[i])

    if browsers[i] != v_browser:
        print("Значение браузера не соответствует, требовалось:", browsers[i], "а получено в ответ", v_browser,
              "неверный UserAgent:", user_agents[i])

    if devices[i] != v_device:
        print("Значение девайса не соответствует, требовалось:", devices[i], "а получено в ответ", v_device,
              "неверный UserAgent:", user_agents[i])

    i += 1



