import random, math

def seater(noOfPlayers,MaxPPT):
    Player = []
    while len(Player) != noOfPlayers:
        name = input("Name of Player: ")
        Player.append(name)
        print("Player", Player[len(Player)-1], "added.\nPlayers playing:", Player)
    random.shuffle(Player)
    NoTables = math.ceil(len(Player)/MaxPPT)
        
    for x in range(0,NoTables):
        print ("Table ",x+1,": " , Player[x::NoTables])
        print ("Player", Player[x] , "is Dealer.")
