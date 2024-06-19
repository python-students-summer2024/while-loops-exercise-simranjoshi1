def get_starting_number():
    while True:
        bottles = input("How many bottles of beer on the wall? ")
        if bottles.isdigit() and int(bottles) >= 1:
             return int(bottles)
        else:
             print("Invalid")


def sing(num_bottles):
    bottles = num_bottles
    while bottles > 0:
        if bottles >2:
            print(str(bottles)+" bottles of beer on the wall, "+str(bottles)+" bottles of beer.\nTake one down, pass it around, "+str(bottles - 1)+" bottles of beer on the wall.\n")
        elif bottles == 2:
            print(str(bottles)+" bottles of beer on the wall, "+str(bottles)+" bottles of beer.\nTake one down, pass it around, "+str(bottles - 1)+" bottle of beer on the wall.\n")
        else:
            print(str(bottles)+" bottle of beer on the wall, "+str(bottles)+" bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall!\n")
        bottles -=1
