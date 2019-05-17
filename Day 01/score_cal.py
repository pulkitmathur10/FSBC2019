##Weighted Score Calculator

##Input the scores obtained in assignments

print("Enter the marks obtained in assignments A1, A2 and A3")

A1 = int(input("A1: "))
A2 = int(input("A2: "))
A3 = int(input("A3: "))

#Input the scores obtained in exams

print("Enter the marks obtained in exams E1 and E2")

E1 = int(input("E1: "))
E2 = int(input("E2: "))

#Calculate the weighted score

weighted_score = ((A1 + A2 + A3) * 0.1) + ((E1 + E2) * 0.35)

print("The weighted score is ")
print(weighted_score)

