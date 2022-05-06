# Write a program to display multiplication table , accept the value of number from the user.
num = int(input("Enter a number : "))
for i in range(1,11):
    print(num,'*',i,'=',num*i)