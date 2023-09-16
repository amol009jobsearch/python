from decimal import Decimal

print("Hello python")

intVar=3
floatVar=3.0
stringVar='India'
decimalVar=Decimal('1.0')

'''check the data types of the variables'''
print(type(intVar))
print(type(floatVar))
print(type(stringVar))
print(type(decimalVar))

print('============')
'''print the values of variable'''
print(intVar)
print(floatVar)
print(stringVar)
print(decimalVar)

print('============')

''' Type casting '''
'''Float to Int conversion'''
objFloat=2.5
convertToInt=int(objFloat)
print(convertToInt)

objInt=2
convertToFloat=float(objInt)
print(convertToFloat)

objInt=5
convertToString=str(objInt)
print(convertToString)
print(type(convertToString))