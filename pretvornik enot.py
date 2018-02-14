# -*- coding: utf-8 -*-
print "Zdravo! Sem program, ki spreminja kilometre v milje.☺ "
x = int(raw_input("Prosim vnesi število kilometrov: "))
y = x * 0.621371
print x, "km je", y ,"milj."
print "Želiš storiti še kakšno pretvorbo?"
z = raw_input()
while z=="da":
    x = int(raw_input("Prosim vnesi število kilometrov: "))
    print x, "km je", y, "milj."
    print "Želiš storiti še kakšno pretvorbo?"
    z = raw_input()
else:
    print "Želim vam lep dan, nasvidenje!"