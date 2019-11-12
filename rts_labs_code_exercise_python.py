# #1  Print the number of integers in an array that are above the given input and the number that are below, e.g. for the array [1, 5, 2, 1, 10] with input 6, print “above: 1, below: 4”.


def Above_and_Below(givenArray, num):
    above = 0
    below = 0
    if len(givenArray) == 0:
        return "you need numbers in your Array!"
    for x in range(len(givenArray)):
        if givenArray[x] > num:
            above += 1
        if givenArray[x] < num:
            below += 1
    return (f'above: {above}, below: {below}')


print(Above_and_Below([1, 5, 2, 1, 10], 6))

# #2  Rotate the characters in a string by a given input and have the overflow appear at the beginning, e.g. “MyString” rotated by 2 is “ngMyStri”.


def questionTwo(givenString, num):
    if num < 0:
        return "You need a positive number to rotate"
    if givenString == "" or givenString == None:
        return "you need to provide a string!"
    num = num % len(givenString)
    print(num)
    tempString = ""
    untouchedString = len(givenString) - num
    x = len(givenString) - 1
    while num > 0:
        tempString = givenString[x] + tempString
        num -= 1
        x -= 1
    for i in range(untouchedString):
        tempString += givenString[i]
    return tempString


print(questionTwo("MyString", 2))

# SECOND AND BETTER WAY


def questionTwoSplit(givenString, num):
    if num < 0:
        return "You need a positive number to rotate"
    if givenString == "" or givenString == None:
        return "you need to provide a string!"
    num = num % len(givenString)
    splitLocation = len(givenString) - num
    answer = ""
    stringArray = [givenString[0:splitLocation],
                   givenString[splitLocation:len(givenString)]]
    x = len(stringArray)-1
    while x >= 0:
        answer = answer + stringArray[x]
        x -= 1
    return answer


print(questionTwoSplit("MyString", 2))
