# -*- coding: utf-8 -*-
import random
seznam_st = []
print "Dobrodošli v generatorju naključnih loto števil."
x = 0
y= int(raw_input("Koliko številk želiš generirati?: "))
while x < y:
    random_st=random.randint(1, 50)
    if random_st not in seznam_st:
        seznam_st.append(random_st)
        x+=1
print seznam_st
print "Konec"
