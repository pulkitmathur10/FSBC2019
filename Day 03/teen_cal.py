#Teen Calculator

def fix_teen(number):
    teen_list = [13,14,17,18,19]
    if number in teen_list:
        return 0
    else:
        return number
def no_teen_sum ( dictionary ):
    list_of_numbers = dictionary.values()
    Sum = 0
    for number in list_of_numbers:
        Sum += fix_teen ( number )
    return Sum


user_input = input("Enter the dictionary input")

splitted_string = user_input.split(',')


splitted_string[0] = splitted_string[0][1:]
splitted_string[len(splitted_string)-1] =splitted_string[len(splitted_string)-1][0:-1] 

dictionary = {}
for i in splitted_string:
    i = i.split(':')
    i[0] = i[0].replace('"','')
    i[1] = int(i[1])
    dictionary[i[0]] = i[1]

print("Sum = " + str(no_teen_sum ( dictionary )))



#import ast
#         
#def fix_teen(n):
#    while n in range(13, 20):
#        if n==15 or n==16:
#            return n
#        else:
#            return 0
#    if n not in range(13, 20):
#        return n
#        
#    
#dict1 = {}
#while True:
#         user_input = input()
##         list1 = []
##         list1.append(user_input)
##         key = []
##         value = []
#         dict1 = ast.literal_eval(user_input)
#        # dict1[key] = int(dict1[key])
#         if user_input == ". .":
#             break
#
#for value in dict1.values():
#        sum = 0
#        x = fix_teen(value)         
#        sum = sum + x
        