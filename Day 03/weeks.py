#Weeks

week_li = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week = tuple(week_li)

usr_in = input("Enter the days of a week ").split(",")

tuple1 = tuple(usr_in)

if tuple1 == week:
     print("All days present")
    
else:
    print(week)    

