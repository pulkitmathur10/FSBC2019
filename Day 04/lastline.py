#Last Line


usr_input = input("Enter file name ")
try:
    print(open(usr_input).readlines()[-1])
except IOError:
    print ( "File not Found or incorrect path")
#except Exception:
  #  print ( "This is a general exception")
#finally:
 #   print ("this is called always")

