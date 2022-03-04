
import random

def test():
    print('ex_nums')
    print(ex_nums())
    print('\n data')
    print(data(isInt=True))

def main():
    e = ex_nums()
    d1 = data()
    d2 = data()
    d3 = data(isInt = False)

    print('##########')
    print('NOT SORTED BY FLOAT')
    print('##########\n')

    for i in range(len(e)):
        print('Experiment {}'.format(e[i]))
        print('Data 1: {}'.format(d1[i]))
        print('Data 2: {}'.format(d2[i]))
        print('Data 3: {}'.format(d3[i]))
        print()

    e, d1, d2, d3 = mergeData(e, d1, d2, d3)

    print('##########')
    print('SORTED BY FLOAT')
    print('##########\n')

    for i in range(len(e)):
        print('Experiment {}'.format(e[i]))
        print('Data 1: {}'.format(d1[i]))
        print('Data 2: {}'.format(d2[i]))
        print('Data 3: {}'.format(d3[i]))
        print()

def mergeData(e, d1, d2, d3, rev_order = False):
    new_list = []
    for i in range(len(e)):
        inner_list = []
        inner_list.append(e[i])
        inner_list.append(d1[i])
        inner_list.append(d2[i])
        inner_list.append(d3[i])
        new_list.append(inner_list)
    
    if rev_order:
        new_list.sort(key=lambda x: -x[3])
    else:
        new_list.sort(key=lambda x : x[3])

    e.clear()
    d1.clear()
    d2.clear()
    d3.clear()

    for l in new_list:
        e.append(l[0])
        d1.append(l[1])
        d2.append(l[2])
        d3.append(l[3])

    return e, d1, d2, d3

def ex_nums(min = 0, num = 50):
    nums = [i + min for i in range(num)]
    return [nums.pop(random.randint(0, len(nums) - 1)) for i in range(num)]

def data(isInt = True, num = 50, min = 100, max = 1000):
    ret_val = []
    if isInt:
        for _ in range(num):
            ret_val.append(random.randint(min, max))
    else:
        for _ in range(num):
            ret_val.append(random.uniform(min, max))
    return ret_val

if __name__ == "__main__":
    main()
