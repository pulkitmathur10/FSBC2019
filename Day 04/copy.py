#Copy Command
#file1 = open("file1.txt" , "wt")
#with open("new.txt", "rt") as fil:
#    file_content = fil.read()
#    file1.writelines(file_content)
#    
#  
#file1.close()



with open("romeo.txt", "rt") as rf:
    with open("file2.txt" , "wt") as wf:
        for line in rf:
            wf.write( line)
    