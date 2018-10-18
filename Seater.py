import random, math

def seater(noOfPlayers,MaxPPT):
    Player = []
    counter = 0
    while counter != noOfPlayers:
        name = input("Name of Player: ")
        Player.append(name)
        print("Player", Player[counter], "added.\nPlayers playing:", Player)
        counter += 1
    random.shuffle(Player)
    NoTables = math.ceil(len(Player)/MaxPPT)
        
    for x in range(0,NoTables):
        print ("Table ",x+1,": " , Player[x::NoTables])
        print ("Player", Player[x] , "is Dealer.")
