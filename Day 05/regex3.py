#Regular Expression 3

import re


while True:
        em_str = input("Enter the card number ")
        if not em_str:
            break
        card_val = re.findall(r'^[456]{1}[\d]{3}-?[\d]{4}-?[\d]{4}-?[\d]{4}', em_str)
        if card_val:
            print("Valid")
        else:
            print("Invalid")
