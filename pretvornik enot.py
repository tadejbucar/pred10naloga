# -*- coding: utf-8 -*-
print "Zdravo! Sem program, ki spreminja kilometre v milje.☺ "
while True:
    x = int(raw_input("Prosim vnesi število kilometrov: "))
    y = x * 0.621371
    print x, "km je", y ,"milj."
    print "Želiš storiti še kakšno pretvorbo? (da/ne)"
    z = raw_input()
    if z=="ne":
        print "Želim vam lep dan, nasvidenje!"
        break
