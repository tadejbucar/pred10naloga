# -*- coding: utf-8 -*-
menu={}
while True:
    x = raw_input("Prosim vnesi jed: ")
    y = raw_input("Prosim vnesi ceno(v €): ")
    menu['Jed'] = x
    menu['Cena(EUR)'] = y
    print "Vnesili ste jed "+ x+ " in ji določili ceno "+y+"€"
    z = raw_input("Ali želite dodati še kakšno jed? (da/ne): ")
    if z=="ne":
        print "Najlepša hvala za sodelovanje."
        break
menu_file = open("menu.txt", "w+")
menu_file.write("Dnevni meni:\n")
for key, value in menu.iteritems():
     menu_file.write("%s: %s\n" % (key, value))
menu_file.close()