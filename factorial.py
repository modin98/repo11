#                   FACTORIAL
#user input type=int display factorial using while loop
num = int(input("pick a number: "))
factorial = 1

while num >1:
    factorial *=num 
    num -=1
print(f'factorial of {num} is {factorial}') 


