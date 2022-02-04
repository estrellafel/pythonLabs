
from calendar import c
import csv
from itertools import count
from operator import itemgetter
from os import sep
from this import d
    
def main():
    f_name = 'data.csv'
    
    # read the csv file contents into a list
    f_in = open(f_name, 'r')
    in_lines = csv.reader(f_in.readlines())
    f_in.close()

    # elements read are strings -- convert to numeric types and store in new list
    # data_lines is the list you will work with
    data_lines = []
    for line in in_lines:
        data_lines.append([float(x) if '.' in x else int(x) for x in line])

    # sorted(list) will return a sorted list while, .sort() will sort the current list
    data_lines.sort(key=lambda x: x[-1])
    print(*data_lines, sep="\n")

    data_lines.sort(key=lambda x: x[-6])
    print(*data_lines, sep="\n")

    # make a list with the size of 50, intitialized to 0
    num_of_type = [0] * 50 
    for i in range(0, 50):
        num_of_type[i] = [i, count(data_lines, i)]
    print(*num_of_type, sep="\n")

    # sort where it is by player type and then average score
    data_lines.sort(key=lambda x: (x[-1], x[-6]))
    print(*data_lines, sep="\n")

def count(data, i):
    retVal = 0
    for e in data:
        if i == e[-1]:
            retVal = retVal + 1
    
    return retVal
        
if __name__ == "__main__":
    main()
