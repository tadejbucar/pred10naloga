# -*- coding: utf-8 -*-
import random
def main():
    skrita_st = random.randint(1, 10)

    while True:
        odgovor = int(raw_input("Skrito število med 1 in 10 je: "))
        if odgovor == skrita_st:
            print "Bravo! Uganil/a si pravo število!☺"
            break
        elif odgovor != skrita_st:
            print "Auč, poskusi znova! ☹"

if __name__ == "__main__":
    main()