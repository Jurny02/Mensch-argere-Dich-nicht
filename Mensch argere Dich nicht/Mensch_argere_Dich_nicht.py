import enum
import random
import time
FIELDSFORPLAYER = 9
class Map:
    def __init__(self, noumberOfPlayers ) -> None:
        self.size = 53
    def CheckFields(self,players,  field, playerNumber ):
        for n, player in enumerate(players):
            if player.PlayerNumber == playerNumber or field > self.size :
                pass
            else:
                for pawnField in player.PawnsPosiotion:
                    if (pawnField + player.PlayerOffset)%(self.size + 1) == field %(self.size + 1)  and  pawnField != 0:
                       players[n].PawnsPosiotion[players[n].PawnsPosiotion.index(pawnField)] = 0;
                       print("Zdezenie na polu nr ",field, "zbija :",playerNumber, " zbity ", player.PlayerNumber)
 

class Player:
    def __init__(self, number, typ):
        self.PlayerNumber = number
        self.PlayerOffset = self.PlayerNumber * FIELDSFORPLAYER
        self.PawnsPosiotion = [0,0,0,0]
        self.Finished = 0 
        self.more = True
        self.WON = False
        self.typ = typ

    def throw(self, more):
        steps = []
        steps.append(random.randint(1,6))
        while steps[-1] == 6 :
            steps.append(random.randint(1,6))
        if more == True and steps.count(6) == 0:
            steps = []
            steps.append(random.randint(1,6))
            while steps[-1] == 6 :
                steps.append(random.randint(1,6))
            if  steps.count(6) == 0:
                steps = []
                steps.append(random.randint(1,6))
                while steps[-1] == 6 :
                    steps.append(random.randint(1,6))
            if steps.count(6) == 0 :
                return [0]
        return steps

    def Play(self): 
        if not self.WON:
            if self.PawnsPosiotion[0] <= 0 and self.PawnsPosiotion[1] <= 0 and self.PawnsPosiotion[2] <= 0 and self.PawnsPosiotion[3] <= 0 and(self.PawnsPosiotion[0] == 0 or self.PawnsPosiotion[1] == 0 or self.PawnsPosiotion[2] == 0 or self.PawnsPosiotion[3] == 0):
                self.more = True
            self.steps = self.throw(self.more)
            self.PawnsPosiotion.sort()
            if self.steps[0] == 0:
                    return -1
            if self.more == True  : #gdy mozna rzucic 3 razy i wypadla 6
                return self.IfMore()
            else:
                if self.typ == 0:
                    self.BigFirst()
                else:
                    self.SmallFirst()
            return -1
    def IfMore(self):
        idx = self.PawnsPosiotion.index(0)
        for x in self.steps[self.steps.index(6) + 1: len(self.steps)]:
            if self.PawnsPosiotion[idx] + x <= 57 - self.Finished:
                self.PawnsPosiotion[idx] += x
                self.more = False
                if self.PawnsPosiotion[idx]  == 57 - self.Finished:
                    self.PawnsPosiotion[idx] = -1
                    self.Finished += 1;
                    if  self.Finished == 4:
                        self.WON = True
        return self.PawnsPosiotion[idx]+ self.PlayerOffset
    def BigFirst(self):
        for index in range (3,-1+self.Finished ,-1):
            if self.PawnsPosiotion[index] > 0 and self.PawnsPosiotion[index] + self.steps[0]  <= 57 - self.Finished :#
                for x in self.steps:
                    if self.PawnsPosiotion[index] + x <= 57 - self.Finished:
                        self.PawnsPosiotion[index] += x
                        if self.PawnsPosiotion[index]  == 57 - self.Finished:
                            self.PawnsPosiotion[index] = -1
                            self.Finished += 1;
                            if  self.Finished == 4:
                                self.WON = True
                return self.PawnsPosiotion[index]+ self.PlayerOffset
        return -1
    def SmallFirst(self):
        for index in range (0+self.Finished,4,1):
            if self.PawnsPosiotion[index] > 0 and self.PawnsPosiotion[index] + self.steps[0]  <= 57 - self.Finished :#
                for x in self.steps:
                    if self.PawnsPosiotion[index] + x <= 57 - self.Finished:
                        self.PawnsPosiotion[index] += x
                        if self.PawnsPosiotion[index]  == 57 - self.Finished:
                            self.PawnsPosiotion[index] = -1
                            self.Finished += 1;
                            if  self.Finished == 4:
                                self.WON = True
                return self.PawnsPosiotion[index] + self.PlayerOffset
        return -1
    def showPosition(self):
        for number, pawn in enumerate(self.PawnsPosiotion):
            print("pionek nr", number, "pozycja :", pawn + self.PlayerOffset , "gracz ", self.PlayerNumber)
        print()




wyniki = [0,0,0,0,0,0]
for x in range (1):
    mapa = Map(6)
    gracze = [Player(0,0),Player(1,0),Player(2,0),Player(3,0), Player(5,0)]
    czy = True
    a = 1
    while czy:
        a+= 1
        for gracz in gracze:
            #gracz.showPosition()
            temp = gracz.Play()
            if temp != -1:
                mapa.CheckFields(gracze, temp , gracz.PlayerNumber)
            gracz.showPosition()
        for gracz in gracze:
            if gracz.WON == True :
                print("Wygral gracz:", gracz.PlayerNumber)
                wyniki[gracz.PlayerNumber] += 1
                czy = False
print (wyniki)





        
