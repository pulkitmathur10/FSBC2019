#Regular Expression 2
import re

lst_1 = []
print("Enter the email addresses: ")
while True:
        em_str = input()
        if not em_str:
            break
        alph_em = re.findall(r'^[a-z\d\-_]+@{1}[a-z\d]+\.{1}[a-z]{2,4}', em_str)
        if alph_em:
            lst_1 = lst_1 + alph_em
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)



natural_sort(lst_1)
print(lst_1)
        



#for email in lst_1:

    
    
    

