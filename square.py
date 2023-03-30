#while loop
#start at 1 end at 100 
#cal and display square of num 
#end loop if ans >2000

num = 1

while num <100:
    ans = num * num
    if ans < 2000:
        num +=1 
        print(f'{num} {ans}')
    else:
        continue 

    