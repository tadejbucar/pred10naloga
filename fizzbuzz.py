# -*- coding: utf-8 -*-
x = int(raw_input("Prosim vnesi število med 1 in 100: "))
for x in range(1, x+1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
        continue
    elif x % 3 == 0:
        print("fizz")
        continue
    elif x % 5 == 0:
        print("buzz")
    else:
         print(x)
