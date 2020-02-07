import random
names = ["Ingrid","Calvin","Margo","Terri","Scott"]
def Football_Squares(names):
    col = 10
    row = 10
    table = [[names[random.randint(0,4)] for i in range(col)] for j in range(row)]
    
    print(str(table))
    for i in range(1,5):
        ints = [int(input("What is the first winning number for quarter " + str(i) + "?")), int(input("What is the second winning number for quarter " + str(i) + "?"))]
        print(str(table[ints[0]][ints[1]]) + " is the winner!")
    
Football_Squares(names)