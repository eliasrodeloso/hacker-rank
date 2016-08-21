mealCost = 0
tipPercent = 0
taxPercent = 0
totalCost = 0

mealCost = float(input(''))
tipPercent = int(input(''))
taxPercent = int(input(''))

def findTip(mealCost,tipPercent):
	percent = 100
	return mealCost*(tipPercent/percent)

def findTax(mealCost, taxPercent):
	percent = 100
	return mealCost*(taxPercent/percent)

def findTotal(mealCost, tip, tax):
	return int(round(mealCost + tip + tax,0))

tip = findTip(mealCost,tipPercent)
tax = findTax(mealCost,taxPercent)
totalCost = str(findTotal(mealCost,tip,tax))

print('The total meal cost is '+totalCost+' dollars.')