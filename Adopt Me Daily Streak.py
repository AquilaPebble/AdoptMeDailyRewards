class Reward:
    def __init__(self,name):
        self.__name = name
        self.__amount = 0
    def __repr__(self):
        return f"{self.Name} : {self.Amount}\n"
    @property
    def Name(self) -> str:
        return self.__name
    @Name.setter
    def Name(self,inputName:str):
        self.__name = inputName
    @property
    def Amount(self) -> int:
        return self.__amount
    @Amount.setter
    def Amount(self,inputAmount:int):
        self.__amount = 0 if inputAmount < 0 else inputAmount
    def resetAmount(self):
        self.Amount = 0
class SystemFunctions:
    @staticmethod
    def findTotal(dailyStreak:int):
        collected = []
        for i in range(0,dailyStreak):
            collected.append(DailyRewards.dailyLoginRewards[i%len(DailyRewards.dailyLoginRewards)])
        return collected
    @staticmethod
    def findSum(inputList:list):
        totalPrice = 0
        for i in inputList:
            if type(i) == int:
                totalPrice += i
            elif type(i) == Reward:
                i.Amount += 1
        return totalPrice
class DailyRewards:
    smallGift = Reward("Small Gift")
    mediumGift = Reward("Medium Gift")
    bigGift = Reward("Big Gift")
    massiveGift = Reward("Massive Gift")
    petwearChest = Reward("Petwear Chest")
    regalPetwearChest = Reward("Regal Petwear Chest")
    crackedEgg = Reward("Cracked Egg")
    dailyLoginRewards = [25,50,100,200,smallGift,25,50,100,200,mediumGift,25,50,100,200,bigGift,25,50,100,200,petwearChest,25,50,100,200,regalPetwearChest,25,50,100,200,massiveGift,25,50,100,200,crackedEgg]
class Main:
    @staticmethod
    def main():
        while True:
            [i.resetAmount() for i in (DailyRewards.smallGift,DailyRewards.mediumGift,DailyRewards.bigGift,DailyRewards.massiveGift,DailyRewards.petwearChest,DailyRewards.regalPetwearChest,DailyRewards.crackedEgg)]
            totalSum = f" $ {SystemFunctions.findSum(SystemFunctions.findTotal(int(input('Daily login streak: '))))}"
            for i in [totalSum,[o for o in (DailyRewards.smallGift,DailyRewards.mediumGift,DailyRewards.bigGift,DailyRewards.massiveGift,DailyRewards.petwearChest,DailyRewards.regalPetwearChest,DailyRewards.crackedEgg) if o.Amount != 0]]:
                print(i)
Main.main()