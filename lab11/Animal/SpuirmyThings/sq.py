
class Squirmy_Things:
    num_st = 3
    def __init__(self):
        # create some member animals
        self.members = ['Worm', 'Snake', 'Octopus']
                
    def add_member(self, new_m):
        self.members.append(new_m)
        Squirmy_Things.num_st += 1

    def delete_member(self, st):
        if st in self.members:
            self.members.remove(st)
            Squirmy_Things.num_st -= 1