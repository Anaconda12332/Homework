user_input=input('Введите слово: ')


if user_input == ''.join(reversed(user_input)):
    print(f"Слово '{user_input}' является палиндромом")