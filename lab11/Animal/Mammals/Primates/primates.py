class Primates:
    num_primates = 3
    def __init__(self):
        # create some member animals
        self.members = ['Monkey', 'Apes', 'Gorillas']
                
    def add_member(self, new_m):
        self.members.append(new_m)
        Primates.num_primates += 1

    def delete_member(self, animal):
        if animal in self.members:
            self.members.remove(animal)
            Primates.num_primates -= 1