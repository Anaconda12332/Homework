a = True
b = False
c = False

print((a or not (a and b) or c), (not a or a and (b or c)), (
    (a or b and not c) and c))
