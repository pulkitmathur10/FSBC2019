# -*- coding: utf-8 -*-

import csv

with open('passwd') as passwd, open('output.csv', 'w') as output:
    r = csv.reader(passwd, delimiter=':')
    w = csv.writer(output, delimiter='\t')
    for record in r:
        if len(record) > 1:
            w.writerow((record[0], record[2]))