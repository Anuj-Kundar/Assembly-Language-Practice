# Write a Python program to check whether an element exists within a tuple
l = input('Enter elements of list : ')
l = l.split()
print('List is : ',l)
for i in l:
    if int(i)%2 == 0:
        l.remove(i)
print('New list : ',l)
l = tuple(input('Enter elements of tuple : '))
x = input('Enter element to search : ')
if x in l:
    print('Element ',x,' is present')
else:
    print('Element ',x,' is not present')

d1 = {1:10,2:20}
d2 = {3:30,4:40}
d3 = {5:50,6:60}
result = {}
result.update(d1)
result.update(d2)
result.update(d3)
print(d1)
print(d2)
print(d3)
print(result)