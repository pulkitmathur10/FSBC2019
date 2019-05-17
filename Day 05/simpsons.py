#Simpsons Phonebook

import re

with open("simpsons_phone_book.txt" , "rt") as sp:
    sph = sp.read()
    sphl = sph.split("\n")
    for cred in sphl:
            simp_neu = re.findall(r'^J{1}[\w]+\s{1}Neu\s{1}[0-9]{3}-[0-9]{3}', cred)
            if simp_neu:
                print(simp_neu)
    