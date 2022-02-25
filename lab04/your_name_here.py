
from xxlimited import new


def main():
    # write your code here
    # you may create additional functions if you like
    names = {'frankenstein.txt':'Elizabeth', 'heart_of_darkness.txt':'Marlow', 
            'romeo_and_juliet.txt':'Capulet', 'war_of_the_worlds.txt':'Ogilvy'}
    username = input('What is your name? ')

    for k in names:
        print('\n'+ k + '\n')
        fn = open('./datafiles/' + k)
        line = fn.readline()
        while line:
            string, num = replace_name_in_line(line, names[k], username)
            if num > 0:
                print(string)
            line = fn.readline()
        fn.close()

def replace_name_in_line(line, name, newName):
    num = 0
    line = line.split()
    for i in range(len(line)):
        if line[i] == name:
            line[i] = newName
            num = num + 1
    return ' '.join(line), num

if __name__ == '__main__':
    main()

