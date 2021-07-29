a, b = 0, 1
while (a or b) < 600:
    a, b = b, a +b
    print(a)
