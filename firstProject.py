import random
aryList = ["cookies","candy","coffee"]

for i in range(3):
    choice = input("What else shall I add?")
    aryList.append(choice)

#print(aryList)
for i in range(6):
    print(aryList[i])
number = random.randint(0,5)
print(aryList[number])