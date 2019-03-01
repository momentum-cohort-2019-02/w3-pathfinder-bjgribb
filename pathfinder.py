import math

class Map:
    def __init__(self, filename):
        self.elevations = []
        with open(filename) as file:
            for row in file:
                self.elevations.append([int(i) for i in row.split()])

        self.max_elevation = max([max(row) for row in self.elevations])
        self.min_elevation = min([min(row) for row in self.elevations])

    def get_elevation_point (self, x, y):
        return self.elevations[y][x]

    def colorIntensity(self, x, y):
        return (self.get_elevation_point(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255

    get intensityArray(self, x, y):
        pass
        


if __name__ == "__main__":

    map = Map('elevation_small.txt')
