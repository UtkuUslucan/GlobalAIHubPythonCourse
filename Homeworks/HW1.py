#GLOBAL AI HUB
#İbrahim Utku USLUCAN
#Homework 1

evenNumbers = list(range(0,20,2))
oddNumbers = list(range(1,20,2))
commonList = evenNumbers + oddNumbers
multipliedList = [i*2 for i in commonList]

print("Even Numbers: " , evenNumbers)
print("Odd Numbers: " , oddNumbers)
print("Common List: " , commonList)
print("Multiplied List: " , multipliedList)

for x in multipliedList:
    print(type(x))
