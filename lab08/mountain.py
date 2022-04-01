class Mountain(object):
    num_mountains = 0

    def __init__(self, name, elevation, prominence, latitude, longitude):
        self.name = name
        self.elevation = elevation
        self.prominence = prominence
        self.latitude = latitude
        self.longitude = longitude
        self.climbed = False
        Mountain.num_mountains = Mountain.num_mountains + 1

    def __del__(self):
        Mountain.num_mountains = Mountain.num_mountains - 1
    
    def is_higher(self, other):
        if(self.elevation > other.elevation):
            return True
        return False

    def climb(self):
        self.climbed = True

    def print_mtn(self):
        print('Name: {}'.format(self.name))
        print('Elevation: {}'.format(self.elevation))
        print('Prominence: {}'.format(self.prominence))
        print('Latitude: {}'.format(self.latitude))
        print('Longitude: {}'.format(self.longitude))
        print('Climbed: {}\n'.format('Yes' if self.climbed else 'No'))
    