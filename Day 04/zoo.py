#Zoo Management
import csv
def read_fl():
        with open("zoo.csv") as zoo_csv:
                zoo_pri = zoo_csv.readlines()
                print(zoo_pri)

#        
def group_sum():
        sum_ele = 0
        sum_tig = 0
        sum_zeb = 0
        sum_lion = 0
        sum_kang = 0   
        with open("zoo.csv") as zoo_group:
                    ani_group = csv.reader(zoo_group, delimiter=",")
                    for row in ani_group:
                            if row[0]=='elephant':
                                sum_ele = sum_ele + int(row[2])
                            elif row[0]=='tiger':
                                sum_tig = sum_tig + int(row[2])
                            elif row[0]=='zebra':
                                sum_zeb = sum_zeb + int(row[2])
                            elif row[0]=='lion':
                                sum_lion = sum_lion + int(row[2])
                            elif row[0]=='kangaroo':
                                sum_kang = sum_kang + int(row[2])    
            
        water_req = []
        water_req = [sum_ele, sum_tig, sum_zeb, sum_lion, sum_kang]
        
        return(water_req) 
                   
def total_water():
    x = list()
    x = group_sum()
    sum=0
    for elem in x:
        sum = sum + elem
    return(sum)    
    
                            
                    
                    
                    
#group_fl()                    
            
            
            
            
            

#with open("zoo.csv") as zoo_group:
#            ani_group = csv.DictReader(zoo_group)
#            for row in ani_group:
#                print ( row['animal'] )
            