#Exception handling for file not found

file = input("Enter the file name that you wish to open: ")
try:
    open(file, 'r')
except FileNotFoundError:
    print("You're not from around here are ya'? That file is all in your mind.")
except:
    print("git!")

#Exception handling for other conditions

num1 = int(input("enter a number: "))
num2 = int(input("enter a divisor: "))

try:
    print(num1/num2)
except FileNotFoundError:
    print("You're not from around here are ya'? That file is all in your mind.")
except SomeException:
    tb = sys.exc_info()[2]
    raise OtherException(...).with_traceback(tb)
except:
    print("git!")
