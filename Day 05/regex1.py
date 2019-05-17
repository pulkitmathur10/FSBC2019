#Regular Expression 1
import re

N = input("Enter the strings: ")
if re.findall(r'\s{0,1}[+-]?\d.\d',N) == None:
    print(False)
else:
    result = re.findall(r'^[+-]?\d.\d',N)
    print(True)
    print(result)
        



