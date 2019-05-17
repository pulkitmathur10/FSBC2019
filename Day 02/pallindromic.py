#Pallindromic Integer

list_int = [12, 90, 61, 51, 14]
temp = []

for value in list_int:
     if value<0:
         print(False)
         break
     if str(value) == str(value)[::-1]:
         print(True)
         break
     else:
         print(False)
         break
         
         
           
     
     

