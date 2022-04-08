class Mountain(object):
    num_mountains = 0

    def __init__(self, name, elevation, prominence, latitude, longitude):
        self.name = name
        self.elevation = elevation
        self.prominence = prominence
        self.latitude = latitude
        self.longitude = longitude
        self.climbed = False
        self.note = ''
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

    def is_climbed(self):
        return self.climbed

    def __gt__(self, other):
        if self.elevation > other.elevation:
            return True
        elif self.elevation < other.elevation:
            return False
        else:
            if self.prominence > other.prominence:
                return True
            else:
                return False
    
    def __lt__(self, other):
        if self.elevation > other.elevation:
            return False
        elif self.elevation < other.elevation:
            return True
        else:
            if self.prominence > other.prominence:
                return False
            else:
                return True
    
    def __bool__(self):
        if self.elevation >= 2000:
            return True
        return False

    def __iadd__(self, gain):
        self.elevation = self.elevation + gain
        return self

    def __isub__(self, loss):
        self.elevation = self.elevation + loss
        return self


    def __str__(self):
        name = 'Name: {}'.format(self.name)
        elevation = 'Elevation: {}'.format(self.elevation)
        prominence = 'Prominence: {}'.format(self.prominence)
        latitude = 'Latitude: {}'.format(self.latitude)
        longitude = 'Longitude: {}'.format(self.longitude)
        climbed = 'Climbed: {}'.format(self.climbed)
        note = 'Note: {}'.format(self.note)
        return '{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(name, elevation, prominence, latitude, longitude, climbed, note)

    def __repr__(self):
        return 'Mountain({},{},{},{},{})'.format(self.name, self.elevation, self.prominence, self.latitude, self.longitude)

    def __call__(self, note):
        self.note = note