##Replacing the chracters

str1 = "RESTART"

#Reverse the string
rstr1 = str1[::-1]
print(rstr1)

#Find the first instance of R and replace with

n_rstr1 = rstr1.replace("R", "$" , 1)

#Reverse again to find required string

n_str1 = n_rstr1[::-1]

print(n_str1)


#Alternate  Method (better)

#input_string = input("Enter your String :")
#
#replaced_char = input("Enter Character which you want to replace :")
#
#replacement_char = input("Enter Character using which you want to replace :")
#
## First occurence of replaced character
#first_occurence = input_string.find(replaced_char)
#
## Replace replaced character with replacement character from input string
#print (input_string[:first_occurence+1] + input_string[first_occurence+1:].replace(replaced_char, replacement_char,1))
#
#








