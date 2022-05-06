# Problem Statement:-
# Write a menu driven program for Exception Handling
# 1. File Handling Exception
# 2. Divide by Zero Exception
# 3. Assert Function

print("1.File handling \n2.Divide by Zero \n3.Assert Function \n4.exit")
while True:
    output=int(input("Output:"))
    # File Handling:
    if(output==1):
        try:
            fd=open("text.txt","r")
            fd.read()
            print("file readed")
        except IOError:
            print("IO exception, file not found")
        else:
            print("No IO exception, file found")
        finally:
            print("finally runned")
    
    # Divide by zero exception:
    elif(output==2):
        try:
            print(1/0)
        except ArithmeticError:
            print("Arithmetic exception")
        else:
            print("No Arithmetic exception")
        finally:
            print("Finally runned")
    
    # Assert Function:
    elif(output==3):
        val=int(input("Value above 0 is:"))
        assert(val>=0),("Value is less than 10")
        print("Value is more than 0, No assertion")
    
    elif(output==4):
        break
    else:
        print("Wrong value")