import math, pprint
from PIL import Image, ImageDraw

class Map:
    def __init__(self, filename):
        self.elevations = []
        with open(filename) as file:
            for row in file:
                self.elevations.append([int(i) for i in row.split()])

        self.max_elevation = max([max(row) for row in self.elevations])
        self.min_elevation = min([min(row) for row in self.elevations])
        self.x_range = len(self.elevations[0])
        self.y_range = len(self.elevations)

    def get_elevation_point(self, x, y):
        return self.elevations[y][x]

    def color_intensity(self, x, y):
        return int((self.get_elevation_point(x, y) - self.min_elevation) / (self.max_elevation - self.min_elevation) * 255)
        
    def draw_elevation_map(self):
        contrast_map = Image.new('RGB', (self.x_range, self.y_range))
        for y in range(self.y_range):
            for x in range(self.x_range):
                rgb_value = self.color_intensity(x, y)
                contrast_map.putpixel((x, y), (rgb_value, rgb_value, rgb_value))
        return contrast_map

    def elevation_point_delta(self):
        cur_x = 0
        cur_y = 300 #midpoint
        path = []
        while cur_x < self.x_range - 1:
            poss_y = [(cur_y)]
            if cur_y - 1 >= 0:
                poss_y.append(cur_y-1)
            if cur_y + 1 < self.y_range:
                poss_y.append(cur_y + 1)

            diffs = [
                abs(self.elevations[poss_y][cur_x + 1] - self.elevations[cur_y][cur_x]) 
                for poss_y in poss_y
                ]

            min_diffs = min(diffs)
            min_diffs_index = diffs.index(min_diffs)
            next_y = poss_y[min_diffs_index]

            cur_x += 1
            cur_y = next_y
            path.append((cur_x, cur_y))
        
        return path

    def draw_path(self):
        contrast_map = Image.open('contrast_map.jpg')
        contrast_map_path = ImageDraw.Draw(contrast_map)
        path = self.elevation_point_delta()
        contrast_map_path.line((path), fill='green')
        contrast_map.save('Pathfinder.jpg')


if __name__ == "__main__":

    map = Map('elevation_small.txt')
    map.draw_path()
    





