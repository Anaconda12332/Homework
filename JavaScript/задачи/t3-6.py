x = False
y = False
z = True

print((x or y and not z), (not x and not y), (not (x and z) or y), (
    x and not y or z), (x and (not y or z)), (x or (not (y or z))))
