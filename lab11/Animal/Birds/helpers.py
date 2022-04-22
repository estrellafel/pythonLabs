def print_members(birds):
    print('Bird list:')
    for m in birds.members:
        print('  {}'.format(m))

def sort_members(birds):
    birds.members.sort()