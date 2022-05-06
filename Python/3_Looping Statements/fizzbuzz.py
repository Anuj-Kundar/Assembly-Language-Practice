# Write a Python program which iterates the integers from 0 to 50. 
# For multiples of three print "APSIT" instead of the number and for the multiples of five print "IT". 
# For numbers which are multiples of both three and five print "APSIT-IT".

for i in range(0,50):
    if i%3 == i%5 == 0:
        print('APSIT-IT')
    elif i%5 == 0:
        print('IT')
    elif i%3 == 0:
        print('APSIT')
    else:
        print(i)
