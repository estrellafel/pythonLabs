import os

def grep(word):
    # your code goes here
    files = [e for e in os.listdir('./datafiles') if not e.startswith('.')]

    for f in files:
        fn = open('./datafiles/' + f, 'r', encoding='utf8')
        line = fn.readline()
        i = 1
        while line:
            if word.lower() in line.lower():
                print(f + ': ' + str(i) + ': ' + line.rstrip())
            i = i + 1
            line = fn.readline()
        fn.close()



def main():
    # call grep from here
    grep('modest')
    grep('love')



if __name__ == '__main__':
    main()


