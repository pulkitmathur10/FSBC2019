#Romeo and Juliet
#from collections import OrderedDict

with open("romeo.txt", "rt") as fp:
    od = {}
    lst7 = []
    list_word = []
    lst7 = fp.readlines()
    for index, element in enumerate(lst7):
        lst7[index] =lst7[index][0:-2]
        list_word = list_word + element.split()
    for value in list_word:
        od[value] = list_word.count(value)
    print(od)
    