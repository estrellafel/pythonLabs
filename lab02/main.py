import os

def main():
    fileName = './datafiles'
    randList = [e for e in os.listdir(fileName) if not e.startswith('.') for x in os.listdir(fileName + '/' + str(e)) if x.split('.')[2] == 'rand']
    evenList = [e for e in os.listdir(fileName) if not e.startswith('.') and int(e.split('.')[1]) % 2 == 0]
    modZeroList = [(x, y) for x in os.listdir(fileName) if not x.startswith('.') for y in os.listdir(fileName) if not y.startswith('.') and (int(x.split('.')[1]) + int(y.split('.')[1])) % 100 == 0]
    randEvenList = []
    for e in randList:
        for f in os.listdir(fileName + '/' + str(e)):
            if not f.startswith('.') and f.split('.')[2] == 'rand':
                fn = open(fileName + '/' + e + '/' + f, 'r')
                num = int(fn.read())
                if num % 2 == 0:
                    randEvenList.append(e)
                fn.close()
    randEvenListComp = [e for e in randList for f in os.listdir(fileName + '/' + str(e)) if not f.startswith('.') and f.split('.')[2] == 'rand' and int(open(fileName + '/' + e + '/' + f, 'r').read()) % 2 == 0]


    #print(*randList, sep='\n')
    #print(*sorted(evenList, key= lambda x: int(x.split('.')[1])), sep='\n')
    #print(*modZeroList, sep='\n')
    #print(*sorted(randEvenList, key= lambda x: int(x.split('.')[1])), sep='\n')
    print(*sorted(randEvenListComp, key= lambda x: int(x.split('.')[1])), sep='\n')




if __name__ == "__main__":
    main()
