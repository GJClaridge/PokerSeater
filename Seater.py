import random
def seater(noOfPlayers):
    Player = []
    counter = 0
    while counter != noOfPlayers:
        name = input("Name of Player: ")
        Player.append(name)
        counter += 1
        random.shuffle(Player)
    if len(Player) >= 9:
        print ("Table 1: " , Player[::2])
        print ("Player", Player[0] , "is Dealer.")
        print ("Table 2: " , Player[1::2])
        print ("Player", Player[1] , "is Dealer.")
    else:
        print(*Player)
        print(Player[0], "is Dealer.")
    
