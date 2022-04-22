def print_members(fish):
    print('Fish list:')
    for m in fish.members:
        print('  {}'.format(m))

def sort_members(fish):
    fish.members.sort()