def devider(num_2):
    
    if num_2 == 1:
        return 1

    else:
        if user_input_1 % num_2 == 0 and user_input_2 % num_2 == 0:
            return num_2
        return devider(num_2-1)
    
     
user_input_1=int(input("Введите первое число: "))
user_input_2=int(input("Введите второе число: "))

print("Наибольший общий делитель:", devider(user_input_2))