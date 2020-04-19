import random as rand

#Random Index Picking
def playerTake(playerList):
    player1Index = rand.randint(0,len(playerList)-1)
    OpponentOne = playerList[player1Index]
    player2Index = rand.randint(0,len(playerList)-1)
    while player2Index == player1Index:
        player2Index = rand.randint(0,len(playerList)-1)
    return player1Index, player2Index

#Correlating Index with Elements
def OpponentChoose():
    player1Index,player2Index = playerTake(playerList)
    Set = [playerList[player1Index],playerList[player2Index]]
    playerList.remove(Set[0])
    playerList.remove(Set[1])
    print("Match is between:",Set)
    return playerList

#Modify this list
playerList = ["Tony","Eric","Jean","Philip","Christin","Suraj","Jose","Joshua","Crystal","Mohammed","Naveen","Rithwik","Varun","Steve"]
count = int(len(playerList)/2)

for i in range (count):
    player1Index,player2index = playerTake(playerList)
    playerList = OpponentChoose()
    playerList= playerList