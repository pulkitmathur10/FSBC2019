#Pallindromic Integer

in_val = input("Enter the Integers:")
inval_lst = in_val.split()

lst_true = [True if i==i[::-1] or int(i)>0 else False for i in inval_lst]
print(all(lst_true))









#lst = []
#
#
#for i in inval_lst:
#    if (i==i[::-1] and int(i)>0):
#        lst.append(True)
#    else:
#        lst.append(False)
#
#print(all(lst))        
 

#def fx(x):
#    if(x==x[::-1] and int(i)>0):       
#my_list = map( :if x==x[::-1] and int(x)>0, inval_lst)
#all(my_list)


