class Painting:
    def __init__(self, name, artist, year):
        self.name = name
        self.artist = artist
        self.year = year

    def __str__(self):
        return f"Painting: {self.name}, {self.artist}, {self.year}"


class Sculpture:
    def __init__(self, name, artist, year):
        self.name = name
        self.artist = artist
        self.year = year

    def __str__(self):
        return f"Sculpture: {self.name}, {self.artist}, {self.year}"