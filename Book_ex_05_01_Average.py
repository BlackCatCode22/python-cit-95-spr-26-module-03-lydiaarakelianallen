#first, we start with no numbers and a total of 0
num= 0
tot= 0
# the next block will allow the user to input as many numbers as they wish
while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    # this ensures that any input has a response and we do not get a traceback error
    except:
        print('Invalid input')
        continue
# this increases the count of valid inputs by 1 for each new input
    num=num+1
# this adds new inputs to our running total
    tot=tot+fval

# this prints out the total of summed values, how many values we collected, and an average of values
print(tot,num, tot/num)