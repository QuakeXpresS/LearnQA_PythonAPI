phrase = input("Set a phrase: ")

assert len(phrase) <= 15, f"Длина вашей строки превышает допустимые 15 символов, в ваше строке сейчас: {len(phrase)} символов"
