import random

class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def playGame(self, name, money):
        self.money -= money
        self.money += name.play(money)

class GameMachine:
    def __init__(self, money):
        self.__money = money
    
    def getMoney(self):
        return self.__money

    def takeMoney(self, money):
        if money >= 0:
            if money > self.__money:
                money = self.__money
                self.__money = 0
            else:
                self.__money -= money
            return money

    def donateMoney(self, money):
        if money >= 0:
            self.__money += money

    def play(self, money):
        self.donateMoney(money)
        value = [i for i in str(random.randint(100, 999))]
        print(value)
        for i in range(1, 3):
            if value.count(value[i]) == 3:
                return self.takeMoney(money*3)
            elif value.count(value[i]) == 2:
                return self.takeMoney(money*2)
        return 0

class Casino:
    def __init__(self, name):
        self.name = name
        self.gameMachineList = []

    def getMoney(self):
        sumMoney = 0
        for machine in self.gameMachineList:
            sumMoney += machine.getMoney
        return sumMoney
    
    def getMachineCount(self):
        return len(self.gameMachineList)

class SuperAdmin(User):
    def __init__(self, *args):
        super().__init__(*args)
        self.casinoDict = {}

    def createCasino(self, casinoName):
        if list(self.casinoDict.keys()).count( casinoName ):
            self.casinoDict.update({ casinoName : Casino(casinoName) })

    def createGameMachine(self, casinoName, money = 0):
        if list(self.casinoDict.keys()).count( casinoName ) == 1 and money >= 0:
            self.casinoDict[casinoName].gameMachineList.append( GameMachine(money) )

    def donateMoneyToMachine(self, money, machineIndex, casinoName):
        self.casinoDict[casinoName].gameMachineList[int(machineIndex)].donateMoney(money)

    def donateMoneyToCasino(self, money, casinoName):
        for machine in self.casinoDict[casinoName].gameMachineList:
            machine.donateMoney(money/self.casinoDict[casinoName].getMachineCount())

    def deleteMachineByIndex(self, index, casinoName):
        money = self.casinoDict[casinoName].gameMachineList.pop(index).getMoney()
        self.donateMoneyToCasino(money, casinoName)

    def sortMachinesByMoney(self, casinoName):
        sortMachineDict = {}
        for machineKey in self.casinoDict[casinoName].gameMachineList:
            sortMachineDict.update({ machineKey : self.casinoDict[casinoName].gameMachineList[machineKey].getMoney() })
        self.casinoDict[casinoName].gameMachineList = list(dict(sorted(sortMachineDict.items(), key=lambda item: item[1], reverse=True)).keys())

    def getMoneyFromCasino(self, money):
        pass

if __name__ == "__main__":
    game1 = GameMachine(300)
    us = User("Andriy", 1000000)
    us.playGame(game1, 100)
    print("user money: {}".format(us.money))
    print("machine money: {}".format(game1.getMoney()))
    list1 = [1, 2, 3]
    buf = list1.pop(1)/2
    list1[1] += buf
    print(list1)

    x = {1: 'A', 3: 'D', 4: 'F', 2: 'C', 0: 'E'}
    print(list(x.keys()))
    print(list(x.values()))
    print(list(dict(sorted(x.items(), key=lambda item: item[1], reverse=True)).keys()))
    
