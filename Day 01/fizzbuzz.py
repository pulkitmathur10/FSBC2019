#Fizz Buzz



i = 0
while i<=100:
    i = i + 1
    if i%15==0: #Divisibility with 3 and 5
        print("FizzBuzz")
    elif i%5==0:#Divisibility with 5
        print("Buzz")
    elif i%3==0:  #Divisibility test with 3
        print("Fizz")
    else:
        print(i)
        
        
    

