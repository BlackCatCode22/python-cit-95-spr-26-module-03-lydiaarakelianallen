# these two lines of code start us off the placeholder None for the largest and smallest number
largest = None
smallest = None
# this block takes user input and protects us from traceback errors from a user entering strings. It builds in "done" as an end to the loop
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
# this replaces smallest's None with the first number entered
    if smallest is None:
        smallest = fnum
# This compares our current smallest to each user entry and replaces smallest with the smallest value when the new value is smaller
    elif fnum < smallest:
        smallest = fnum

# this replaces largest's None with the first number entered
    if largest is None:
        largest = fnum
# this compares our current largest to each user entry and replaces fnum with the largest value when the new value is larger
    elif fnum > largest:
        largest = fnum

# this prints the maximum and minimum from the list of values that the user entered.
print("Maximum is", int(largest))
print("Minimum is", int(smallest))