class Reward:
    def __init__(self,name):
        self.name = name
        self.amount = 0
    def __repr__(self):
        return f"{self.name} : {self.amount}\n"
    def resetAmount(self):
        self.amount = 0
def findTotal(dailyStreak:int,dailyLoginRewards:list):
    collected = []
    for i in range(0,dailyStreak):
        collected.append(dailyLoginRewards[i%len(dailyLoginRewards)])
    return collected
def findSum(inputList:list):
    totalPrice = 0
    for i in inputList:
        if type(i) == int:
            totalPrice += i
        elif type(i) == Reward:
            i.amount += 1
    return totalPrice
# GIFTS
smallGift = Reward("Small Gift")
mediumGift = Reward("Medium Gift")
bigGift = Reward("Big Gift")
massiveGift = Reward("Massive Gift")
petwearChest = Reward("Petwear Chest")
regalPetwearChest = Reward("Regal Petwear Chest")
crackedEgg = Reward("Cracked Egg")
# MAIN
dailyLoginRewards = [25,50,100,200,smallGift,25,50,100,200,mediumGift,25,50,100,200,bigGift,25,50,100,200,petwearChest,25,50,100,200,regalPetwearChest,25,50,100,200,massiveGift,25,50,100,200,crackedEgg]
while True:
    [i.resetAmount() for i in (smallGift,mediumGift,bigGift,massiveGift,petwearChest,regalPetwearChest,crackedEgg)]
    totalSum = f" $ {findSum(findTotal(int(input('Daily login streak: ')),dailyLoginRewards))}"
    for i in [totalSum,[o for o in (smallGift,mediumGift,bigGift,massiveGift,petwearChest,regalPetwearChest,crackedEgg) if o.amount != 0]]:
        print(i)