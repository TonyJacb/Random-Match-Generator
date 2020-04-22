import random as rand

#Returns the list of players
def viewPlayers():
    return playerList

#Random Index Picking
def playerTake(playerList):
    player1Index = rand.randint(0,len(playerList)-1)
    player2Index = rand.randint(0,len(playerList)-1)            #Randomly picks out incices
    while player2Index == player1Index:
        player2Index = rand.randint(0,len(playerList)-1)        #Doesn't enable same person to face with each other
    return player1Index, player2Index

#Correlating Index with Elements
def OpponentChoose():
    player1Index,player2Index = playerTake(playerList)          #Retrives indices from the previous function
    Set = [playerList[player1Index],playerList[player2Index]]   #Sets match
    playerList.remove(Set[0])
    playerList.remove(Set[1])                                   #Deletes them from the original list
    return playerList, Set

#Main Function
def matchView(count,playerList):
    matches=[]
    for i in range (count):                                     #Iterates till max number of 1v1 matches can be made
        player1Index,player2index = playerTake(playerList)
        playerList, Set = OpponentChoose()
        matches.append(Set)
        playerList= playerList
    return matches                                  #New list without the already chosen players is passed to iterate again

#Modify this list
playerList = [
    "Tony","Eric","Jean","Philip","Christin","Suraj","Jose","Joshua","Crystal","Mohammed","Naveen","Rithwik","Varun","Steve"
            ]
count = int(len(playerList)/2)
