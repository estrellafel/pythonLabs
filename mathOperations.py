import math

# Use 4 4's to print out 0 through 20
def fourFours():
    print('4 - 4 + 4 - 4 = {}'.format(4 - 4 + 4 - 4))
    print('4 // 4 * 4 // 4 = {}'.format(4 // 4 * 4 // 4))
    print('4 // 4 + 4 // 4 = {}'.format(4 // 4 + 4 // 4))
    print('4 // int(math.sqrt(4)) + 4 // 4 = {}'.format(4 // int(math.sqrt(4)) + 4 // 4))
    print('int((4 * 4) / math.sqrt(4)) - 4) = {}'.format(int((4 * 4) / math.sqrt(4)) - 4))
    print('int(4 / 4 + math.sqrt(4) + math.sqrt(4)) = {}'.format(int(4 / 4 + math.sqrt(4) + math.sqrt(4))))
    print('int(4 - 4 + 4 + math.sqrt(4)) = {}'.format(int(4 - 4 + 4 + math.sqrt(4))))
    print('4 + 4 - 4 // 4 = {}'.format(4 + 4 - 4 // 4))
    print('4 + 4 + 4 - 4 = {}'.format(4 + 4 + 4 - 4))
    print('4 + 4 + 4 // 4 = {}'.format(4 + 4 + 4 // 4))
    print('int(4 * 4 - 4 - math.sqrt(4)) = {}'.format(int(4 * 4 - 4 - math.sqrt(4))))
    print('int(math.factorial(4) // math.sqrt(4) - 4 // 4) = {}'.format(int(math.factorial(4) // math.sqrt(4) - 4 // 4)))
    print('4 * int((math.sqrt(4) + 4 // 4)) = {}'.format(4 * int((math.sqrt(4) + 4 // 4))))
    print('int(4 // 4 +  math.factorial(4) // math.sqrt(4)) = {}'.format(int(4 // 4 +  math.factorial(4) // math.sqrt(4))))
    print('4 * 4 - 4 // 4 = {}'.format(int(4 * 4 - 4 // math.sqrt(4))))
    print('int(4 * 4 - 4 // math.sqrt(4)) = {}'.format(4 * 4 - 4 // 4))
    print('4 * 4 + 4 - 4 = {}'.format(4 * 4 + 4 - 4))
    print('int(4 * 4 + 4 // math.sqrt(4)) = {}'.format(4 * 4 + 4 // 4))
    print('int(4 * 4 + 4 - math.sqrt(4)) = {}'.format(int(4 * 4 + 4 - math.sqrt(4))))
    print('math.factorial(4) - 4 - 4 // 4 = {}'.format(math.factorial(4) - 4 - 4 // 4))
    print('math.factorial(4) - 4 + 4 - 4 = {}'.format(math.factorial(4) - 4 + 4 - 4))

# Some practice with list
def listPrac():
    #Create a list of 1-20, evens in 1-20 and odds in 1-20
    nums = [x for x in range(0, 21)]
    evens = [x for x in range(0, 21) if x % 2 == 0]
    odds = [x for x in range(0,21) if x % 2 != 0]

    # *list will print without the brackets and commas but list will print with brackets and commas
    # sep allows the programmer to put something inbetween the elements when printing
    print(*nums, sep="\n")
    print(*evens)
    print(*odds)

if __name__ == '__main__':
    fourFours()
    # listPrac()