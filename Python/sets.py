import random 

myList = []
mySet = set()

for x in range(0, 100):	
	myList.append(random.randint(0, 50))
print(myList)

for x in myList:
	mySet.add(x)

print(mySet)