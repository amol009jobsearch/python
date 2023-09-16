objStr = 'India is my country'
print(objStr)

'''Iterate over string object'''
for i in objStr:
    print("each char of string = ",i)

'''Below code to calculate the length of string'''
print(len(objStr))

'''Place holder replacement using format method'''
greetings="Hi {}, How are you?"
#print(greetings.format('Amol'))

listOfNames=['Amol','Nachiket','Aniket','Shashi']

for i in listOfNames:
    print(greetings.format(i))





