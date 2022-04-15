class Character(object):
    def __init__(self, first_name, last_name, evil_count):
        self.first_name = first_name
        self.last_name = last_name
        self.evil_count = evil_count

    def increment_evil_count(self, cersei_effect = False):
        if cersei_effect == True:
            self.evil_count = self.evil_count + 2
        else: 
            self.evil_count = self.evil_count + 1

    def name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.last_name, self.evil_count)