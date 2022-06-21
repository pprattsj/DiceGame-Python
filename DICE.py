import random

class Dice:
        def __init__(self,sides,color):
                self.sides=sides-1
                self.color=color
        def Describe(self):
                print(self.sides,self.color)

        def DieRoll(self):
                return random.randint(0,self.sides)

        def Rolls(self,times):
                results =[]
                for x in range(times):
                        results.append(self.DieRoll())
                return(results)
        def FreqTest(self,r):
                zero,one,two,three,four,five = 0,0,0,0,0,0
                for x in r:
                        if (x==0): zero+=1
                        if (x==1): one+=1
                        if (x==2): two+=1
                        if (x==3): three+=1
                        if (x==4): four+=1
                        if (x==5): five+=1
                print(zero,one,two,three,four,five)

class Tile:
	def __init__(self):
		self.Value =0
		self.PrevPos =0
		self.Pos=0
	def isNew(self):
		return(self.PrevPos==0)
	def hasChanged(self):
		return(self.PreValue!=self.Value)
	def shallAnimate(self):
		return(self.isNew() or self.hasChanged())

def example():
        
        r=[]
        print("make a purple 6-sided die :gem = Dice(6,\"purple\")")
        gem = Dice(6,"purple")
        print("roll purple die 20 times: r=gem.Rolls(20)")
        r=gem.Rolls(20)
        r.append(0)
##r.append(19)
        for x in r :
                if (x ==gem.sides):
                        print ("Critical Hit! :)")
                elif (x ==0):
                        print ("Critical Flub ! :(")
                else: print(x+1)

        print("check freq distribution across 1st 6 values")
        gem.FreqTest(r)
