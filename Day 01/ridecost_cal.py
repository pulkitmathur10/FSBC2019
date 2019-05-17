
##Ride Cost Calculator

#Distance Traveled per day

dist_day = int(input("Enter the distance traveled in a day "))

#Average Fuel Consumption
average = int(input("Enter the average fuel consumed by vehicle "))

#Cost of Diesel per litre

diesel_cost = int(input("Enter the diesel cost per litre "))


#Calculation of Cost of Driving per day

cost = (dist_day/average) * diesel_cost

print("The cost of driving to the office per day is")
print(cost)