#GLOBAL AI HUB
#İbrahim Utku USLUCAN
#Homework 1

evenNumbers = list(range(0,20,2))
print(evenNumbers)

oddNumbers = list(range(1,20,2))
print(oddNumbers)

commonList = evenNumbers + oddNumbers
print(commonList)

multiplyList = [i*2 for i in commonList]
print(multiplyList)

for x in multiplyList:
    print(type(x))
