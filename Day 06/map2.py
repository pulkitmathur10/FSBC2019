
names = ['Mary', 'Isla', 'Sam']

code_id = list(map(lambda i:hash(i) , names))
print(code_id)