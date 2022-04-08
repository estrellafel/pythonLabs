from mountain import Mountain

def main():
    swiss_mountains = []
    fn = open('./mountains.txt')
    line = fn.readline()
    while(line):
        split_line = line.split()
        swiss_mountains.append(Mountain(split_line[0], int(split_line[1]), int(split_line[2]), split_line[3], split_line[4]))
        line = fn.readline()
    swiss_mountains[1].climb()
    swiss_mountains[15].climb()
    # check_higher(swiss_mountains)
    # print_mountains(swiss_mountains)
    # check_num(swiss_mountains)
    check_is_climbed(swiss_mountains)
    check_signs(swiss_mountains)
    check_str(swiss_mountains)

def check_is_climbed(swiss_mountains):
    print(swiss_mountains[1].is_climbed())

def check_signs(swiss_mountains):
    print(swiss_mountains[0] > swiss_mountains[1])
    print(swiss_mountains[0] < swiss_mountains[1])
    print('Correct' if swiss_mountains[0] else 'Wrong')
    print('Elevation is {}'.format(swiss_mountains[0].elevation))
    swiss_mountains[0] += 200
    print('Add 200 {}'.format(swiss_mountains[0].elevation))
    swiss_mountains[0] -= 200
    print('Minus 200 {}'.format(swiss_mountains[0].elevation))

def check_str(swiss_mountains):
    swiss_mountains[0]('YES')
    print(swiss_mountains[0])
    print(repr(swiss_mountains[0]))

    

def check_higher(swiss_mountains):
    if(swiss_mountains[0].is_higher(swiss_mountains[1])):
        print('is_higher, works properly :)\n')
    else:
        print('is_higher does not work properly :(\n')

def print_mountains(swiss_mountains):
    for e in swiss_mountains:
        e.print_mtn()

def check_num(swiss_mountains):
    print('16: {}\n'.format(swiss_mountains[0].num_mountains))
    del swiss_mountains[8]
    print('15: {}\n'.format(swiss_mountains[0].num_mountains))
    del swiss_mountains[14]
    print('14: {}\n'.format(swiss_mountains[0].num_mountains))
    while len(swiss_mountains) > 1:
        del swiss_mountains[0]
    print('1: {}\n'.format(swiss_mountains[0].num_mountains))

    
if __name__ == "__main__":
    main()