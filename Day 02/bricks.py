#Bricks


def brickTarget(small, big, target):
    if target%5<=small:
      length = big*5 + small
      if(length>=target):
          print(True)
      else:
          print(False)
    else:
        print(False)
    

brick_str= input("Enter the number of small bricks, medium bricks and target (with space) ").split()
brick_list = []
for el in brick_str:
    brick_list.append(int(el))

brickTarget(brick_list[0], brick_list[1], brick_list[2])