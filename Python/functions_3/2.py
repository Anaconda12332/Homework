import random

def play(user_num, counter):
    
    user_num=input("Введите число: ")

    if user_num == number:
        print("Win!")

    else:
        quantity=set()
        right_place=0 

        for i in user_num:  
            if i in number:
                quantity.add(i) 

        for i, j in zip(user_num, number):
            if i == j:
                right_place += 1
            
        counter += 1
        print(f"Угадано чисел: {len(quantity)}")
        print(f"Чисел на своих местах: {right_place}")
        print(f"Использовано попыток: {counter}")

        return play(user_num, counter)

number= str(random.randint(1000, 9999))
   
counter=0

play("Start the game",0)


