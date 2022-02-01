from math import sqrt


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.cluster_index = -1

    def __str__(self) -> str:
        return f"x = {self.x}; y = {self.y}"

    def calc_distance(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
