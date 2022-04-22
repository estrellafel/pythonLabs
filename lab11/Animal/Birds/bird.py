class Bird:
    num_birds = 3
    def __init__(self):
        # create some member animals
        self.members = ['Crow', 'Blue Jay', 'Cardinal']
                
    def add_member(self, new_m):
        self.members.append(new_m)
        Bird.num_birds += 1

    def delete_member(self, animal):
        if animal in self.members:
            self.members.remove(animal)
            Bird.num_birds -= 1