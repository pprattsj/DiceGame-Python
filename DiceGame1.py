## DICE GAME

## Create Players
## Assign Dice
    ### copy player diceset.color to availDice
    ### Collect bankdice upto len(availDice)
        ### bankdice.append(input)
        ### availDice.remove(input)
    ### Collect defencedice upto len(availDice)
    ### Collect AttackDice upto len(availDice)
## Roll Dice by groups
    ### total=0
    ### for x in bankdice
        ### for die in diceset
            ### if (dice.color==x):
                ### total=total + die.Rolls((1)[0]+1


import DICE
class Zone:
    def __init__(self,zonetype):
        self.zonetype=zonetype
        self.zoneDice=[]
        self.rolltotal=0
    
class Player:
    def __init__(self,name):
        self.name=name
        self.lives=20
        self.diceset=[]
        self.diceset.append(DICE.Dice(4,"yellow"))
        self.diceset.append(DICE.Dice(4,"red"))
        self.diceset.append(DICE.Dice(4,"blue"))
        self.zoneset=[]
        self.zoneset.append(Zone('BANK'))
        self.zoneset.append(Zone('ATTACK'))
        self.zoneset.append(Zone('DEFENCE'))
        self.zoneset.append(Zone('HOSPITAL'))
        print("Player",self.name," has 3 4-sided dice,no bank, and 20 Life points")

    def add_dice(self,sides,color):
        self.diceset.append(DICE.Dice(sides,color))

    def remove_dice(self, color):
        pass

    def Zone_Stat(zone):
         print(zone)


    
def createAvailDice(player,availset):
    print(availset)
    availset.clear()
    print("availset is blank:",availset)
    
    print(len(player.diceset))
    for x in range(0,len(player.diceset)):
        availset.append(player.diceset[x].color)
    print(availset)
        
                        
def assignDice(availDice,zone):
    zone.zoneDice.clear()
    while len(availDice) > 0:
        i= input("which dice to assign?")
        if (i==''):
            break
        elif (i in availDice):
            zone.zoneDice.append(i)
            availDice.remove(i)
        else :
            print("unknow reponse")


def rollZone(player, zone):
    zone.rolltotal=0
    for x in zone.zoneDice:
        for die in player.diceset:
            if (die.color == x):
                zone.rolltotal += die.Rolls(1)[0]+1

    
            


## players=[]
## players.append(Player("Paul"))
## players[0].availDice =[]
## createAvailDice(players[0],players[0].availDice)
## for x in players[0].zoneset
##      assignDice(players[0].availDice,x)
##? for x in players[0].zoneset
##?      rollZone(players[0],x
                
                            


