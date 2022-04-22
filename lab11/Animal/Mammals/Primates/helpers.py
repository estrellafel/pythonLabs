def print_members(primate):
    print('Primate list:')
    for m in primate.members:
        print('  {}'.format(m))

def sort_members(primate):
    primate.members.sort()