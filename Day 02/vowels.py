#Vowels Finder

state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
final_list = []
vowels = ['a', 'e', 'i', 'o', 'u']

for state in state_name:
    temp_str = []
    for letter in state.lower():
        if letter not in vowels:
            temp_str.append(letter)
    final_list.append("".join(temp_str))
print(final_list)
    
    
    
    


#state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
#final_list = []
#vowels = ['a', 'e', 'i', 'o', 'u']
#
#for state in state_name:
#    temp_str = ""
#    for letter in state.lower():
#        if letter not in vowels:
#            temp_str = temp_str + letter
#    final_list.append(temp_str)
#
#print(final_list)