def get_starting_number():
    while True:
        bottles = input("How many bottles of beer on the wall? ")
        if bottles.isdigit() and int(bottles) >= 1:
             return int(bottles)
        else:
             print("Invalid")


def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i > 2:
            print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.")
            print("Take one down, pass it around, " + str(i-1) + " bottles of beer on the wall.\n")
        elif i == 2:
            print(str(i) + " bottles of beer on the wall, " + str(i) + " bottles of beer.")
            print("Take one down, pass it around, " + str(i-1) + " bottle of beer on the wall.\n")
        else:
            print(str(i) + " bottle of beer on the wall, " + str(i) + " bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!")
