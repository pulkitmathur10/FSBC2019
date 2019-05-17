#create a list of absentee

with open("absentee.txt", "wt") as fp:


        lst1 = []
        print("Enter the names of absentees")
        for entry in range(1, 26):
            name = input()
            if not name:
                break
            lst1.append(name)
    
    

