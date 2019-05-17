#Pattern Builder

num_stars = int(input("Enter the number of asterisk iterations"))
for value in range(1, num_stars+1):
    print("* "*value)
    if(value==num_stars):
        for value in range(num_stars-1, 0, -1):
          print("* "*value)
        
        
        
    
