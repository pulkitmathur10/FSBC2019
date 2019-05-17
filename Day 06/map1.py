# -*- coding: utf-8 -*-

import random

names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

sec_name = list(map(lambda i:random.choice(code_names) , names))
print(sec_name)


    