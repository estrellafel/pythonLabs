from character import Character
import utilities as ut

def main():
    data = ut.read_characters('./characters.txt')
    players = fill_players(data)
    ut.print_menu(players)
    print()
    players = evil(players)
    most_evil(players)

def fill_players(data):
    players = {}
    i = 0
    while i < len(data):
        c = Character(data[i], data[i+1], 0)
        players[data[i + 2]] = c
        i = i + 3
    return players

def evil(players):
    flag = True
    while flag:
        k = input('Enter key for character: ')
        if k.lower() == 'quit':
            flag = False
        elif k in players:
            print()
            if players[k].first_name.lower() == 'cersei' and players[k].last_name.lower() == 'lannister':
                print('EVIL EVIL EVIL')
                players[k].increment_evil_count(cersei_effect = True)
            else:
                players[k].increment_evil_count()
            print("{}'s evil count has been changed".format(players[k].name()))
            print()
        else:
            print('\nNot a valid key')
            print()
    return players

def most_evil(players):
    worst_score = -1
    worst = []
    for k, v in players.items():
        if v.evil_count > worst_score:
            worst.clear()
            worst.append(k)
            worst_score = v.evil_count
        elif v.evil_count == worst_score:
            worst.append(k)
    
    print('\n************************************************')
    if len(worst) == 1:
        print('The worst is {}.'.format(players[worst[0]].name()))
    else:
        print('The worst are:')
        for e in worst:
            print('    {}'.format(players[e].name()))
    print('************************************************')
    print()
    
if __name__ == "__main__":
    main()