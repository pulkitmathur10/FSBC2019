# -*- coding: utf-8 -*-

users = {} 
with open('passwd') as f_us:
    for line in f_us:
        if not line.startswith("_"):
            user_info = line.split(":")
            users[user_info[0]] = user_info[2]
 
print(users)