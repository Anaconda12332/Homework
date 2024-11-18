range_num=list(map(str, (range(100, 10000))))

formatted=[]
for i in range_num:
    if len(i) == 4:
        if len(set(n for n in i)) != 4:
           None
        else:
         formatted.append(int(i))

    elif len(i) == 3:
        if len(set(n for n in i)) != 3:
            None
        else:
            formatted.append(int(i))

print(len(formatted))