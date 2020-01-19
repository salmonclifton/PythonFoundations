#Generate a random number between 50 and 100 and store
import random
test_num = random.randint(50,100)
#Display 'fizzbuzz!' if test_num is divisible by both 3 and 5
if (test_num%3) == 0 and (test_num%5) == 0:
    print("fizzbuzz!")
#Display 'buzz!' if test_num is divisible by 5
elif (test_num%5) == 0:
    print("buzz")
#Display 'fizz!' if test_num is divisible by 3
elif (test_num%3) == 0:
    print("fizz")
#Otherwise display the value
else:
    print (test_num)