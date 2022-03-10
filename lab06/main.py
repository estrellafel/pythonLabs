#
# CS 224 Spring 2022
# Programming Lab 6
# 
# Will generate data, at random, for experiments and then sort it as specified.
#
# Author: Felix Estrella
# Date: March 10, 2022
#

import random

def main():
    ex_nums = generate_experiment(50)
    data_1 = generate_data()
    data_2 = generate_data()
    data_3 = generate_data(is_int = False)

    print('Initial Data\n')
    output(ex_nums, data_1, data_2, data_3)

    ex_nums, data_1, data_2, data_3 = order(ex_nums, data_1, data_2, data_3, False)

    print('Final Data\n')
    output(ex_nums, data_1, data_2, data_3)

def generate_experiment(num):
    return [e for e in range(num)]

def generate_data(is_int = True, num = 50, min = 100, max = 1000):
    ret_val = []
    if is_int:
        for _ in range(num):
            ret_val.append(random.randint(min, max))
    else:
        for _ in range(num):
            ret_val.append(random.uniform(min, max))
    return ret_val

def output(ex_nums, data_1, data_2, data_3):
    for i in range(len(ex_nums)):
        print('Experiment Number: {}'.format(ex_nums[i]))
        print('Data 1: {}'.format(data_1[i]))
        print('Data 2: {}'.format(data_2[i]))
        print('Data 3: {}\n'.format(data_3[i]))

def order(ex_num, data_1, data_2, data_3, rev_order):
    comb_list = list(zip(ex_num, data_1, data_2, data_3))
    comb_list.sort(key=lambda x: -x[1]) if rev_order else comb_list.sort(key=lambda x: x[1])
    ex_num = remake_list(comb_list, 0)
    data_1 = remake_list(comb_list, 1)
    data_2 = remake_list(comb_list, 2)
    data_3 = remake_list(comb_list, 3)
    return ex_num, data_1, data_2, data_3

def remake_list(l, index):
    ret = []
    for i in range(len(l)):
        ret.append(l[i][index])
    return ret

if __name__ == "__main__":
    main()