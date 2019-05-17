#Regular Expressions 4

import re
lst_1 = []
while True:
        em_str = input("Enter the email addresses: ")
        if not em_str:
            break
        alph_em = re.findall(r'^[a-z0-9\-_]+@{1}[a-z0-9]+\.{1}[a-z]{2,4}', em_str)
        if alph_em:
            lst_1 = lst_1 + alph_em
print(sorted(lst_1))

