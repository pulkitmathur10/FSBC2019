#Book Shop

list1 =[ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
         ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
         ["77226", "Head First Python, Paul Barry", 3,32.95],
         ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]

#prod_list=[]
#for values in list1:
#    ord_no = values[0]
#    prod=values[2]*values[3]
#    if prod<100:
#        prod=prod+10
#    else:
#        prod
#    prod_list.append((ord_no,prod))
#
#
#        
#print(prod_list)
#

bill_summary = list(map(lambda values: values if values[1]>=100 else (values[0], values[1] +10), 
                    map(lambda values: (values[0], round(values[2]*values[3],2)) , list1)))
print(bill_summary)
         
        
        
        

        
        

