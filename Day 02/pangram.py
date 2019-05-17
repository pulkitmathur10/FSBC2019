#Pangram

#import string

def Pangram(str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for char in alpha:
        if char in str.lower():
            return True
        
    return False
            


if(isPangram("The five boxing wizards jumps") == False):
  print("Not Pangram")
else:
  print("Pangram")           