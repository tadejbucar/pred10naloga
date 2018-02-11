# -*- coding: utf-8 -*-

secret = 10
guess = int(raw_input("Skrito število je: "))
if guess == secret:
    print "Bravo! Uganil/a si pravo število!☺"
else:
    print "Auč, poskusi znova! ☹"