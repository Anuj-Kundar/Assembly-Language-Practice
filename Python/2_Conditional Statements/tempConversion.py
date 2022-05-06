# Write a Python program to convert temperatures to and from Celsius, Fahrenheit.
temp = input('Enter Temp : ')
degree = int(temp[:-1])
typ = temp[-1]
if typ.upper()=='C':
    temp1 = round(degree*9/5)+32
    result='F'
elif typ.upper()=='F':
    temp1 = round((degree-32)/9*5)
    result='C'
else:
    print('Invalid input.')
    quit()

print('Converted temp is ',temp1,result)