def sort(lists):
    if sum(lists)/len(lists) > 0:
        
        sort_2=lists[:len(lists)*2//3]
        sort_1=lists[len(lists)*2//3:]
        
    else:
        sort_2=lists[:len(lists)//3]
        sort_1=lists[len(lists)//3:]

    print(*sorted(sort_2),"\n",*sort_1[::-1])
    

user_input=list(map(int, input("Введите числа разделенные пробелом: ").split()))

sort(user_input)
