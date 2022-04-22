def print_members(st):
    print('Squirmy Things list:')
    for m in st.members:
        print('  {}'.format(m))

def sort_members(st):
    st.members.sort()