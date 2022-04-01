from mountain import Mountain

def main():
    swiss_mountains = []
    fn = open('./mountains.txt')
    line = fn.readline()
    while(line):
        split_line = line.split()
        swiss_mountains.append(Mountain(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4]))
        line = fn.readline()
    swiss_mountains[1].climb()
    check_higher(swiss_mountains)
    print_mountains(swiss_mountains)
    check_num(swiss_mountains)

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