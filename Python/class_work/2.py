user_input=input('Введите текст: ')
user_input_2=input('Введите зарезервированные слова: ')


if user_input_2 in user_input:
    user_up=user_input.replace(user_input_2, user_input_2.upper())
    print(user_up)
