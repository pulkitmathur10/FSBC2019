#Supermarket

from collections import OrderedDict


# make Object of OrderDict
od = OrderedDict()

while True:
    # take items from user as input
    user_input = input("Enter item with price : ")

    if not user_input:
        break
    
    # use split function to get item's price value
    temp = user_input.split()
    price = temp[-1]
    
    # join rest string which is item name
    item = " ".join(temp[:-1])
    
    # Adding and updating price of the item using orderdict function 
    od[item] = od.get(item,0) + int(price)

for k,v in od.items():
    print (k,v)
















#in_items = dict()
#
#print("Enter key and value separated by space: ")
#while True:
#         user_input = input()
#         key, value = user_input.split(" ")
#         in_items[key] = value
#         if not user_input:
#             break
#if value in in_items:
#    in_items[value] = in_items[value]
             
        



