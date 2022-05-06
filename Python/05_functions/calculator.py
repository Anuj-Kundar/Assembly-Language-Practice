def Add(n1,n2):
    sum1 = n1 + n2
    return sum1
def Diff(n1,n2):
    diff = n1 - n2
    return diff
def mul(n1,n2):
    mul = n1 * n2
    return mul
def div(n1,n2):
    div = n1 / n2
    return div
def mod(n1,n2):
    mod = n1 % n2
    return mod
x,y = input("Enter 2 numbers : ").split()
ch = input("Enter operator : ")
if ch=='+':
    res=Add(int(x),int(y))
    print(res)
elif ch=='-':
    res=Diff(int(x),int(y))
    print(res)
elif ch=='*':
    res=mul(int(x),int(y))
    print(res)