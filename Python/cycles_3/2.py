range_num=list(map(str, (range(100, 1000))))

formatted=[]
for i in range_num:
   for m in i:
    if i.count(m) > 1:
        formatted.append(int(i)) if i not in formatted else None

print(len(formatted))