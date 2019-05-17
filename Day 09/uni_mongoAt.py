#Uni Mongo Atlas

import pymongo

client = pymongo.MongoClient("mongodb://pulkitmathur10:pulkit123@cluster-pulkit-shard-00-00-j3koo.mongodb.net:27017,cluster-pulkit-shard-00-01-j3koo.mongodb.net:27017,cluster-pulkit-shard-00-02-j3koo.mongodb.net:27017/test?ssl=true&replicaSet=Cluster-Pulkit-shard-0&authSource=admin&retryWrites=true")

mydb = client.db_uni1

def add_student(name, age, roll_no, branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.students.uni.insert_one(
            {
            "Student_Name" : name,
            "Student_age" : age,
            "Student_Roll_No" : roll_no,
            "Student_Branch" : branch
            })
    return "Student Added Successfully"

def fetch_all_students():
    user = mydb.students.uni.find()
    for i in user:
        print (i)
        
add_student('Pulkit Mathur', 20, 129, 'CSE')
add_student('Jon Snow', 26, 130, 'CSE')
add_student('Sansa Stark', 24, 131, 'CSE')
add_student('Daenerys Targaryen', 26, 132, 'CSE')
add_student('Arya Stark', 22, 133, 'IT')
add_student('Bran Stark', 20, 134, 'IT')
add_student('Tyrion Lannister', 31, 135, 'ECE')
add_student('Lord Varys', 40, 136, 'ECE')


fetch_all_students()        