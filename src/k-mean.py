from random import randint
import sys

import matplotlib.pyplot as plt
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


CLUSTER_COUNT = 5
MAX_AXIS_VALUE = 100
POINT_COUNT = 5000
points = [Point(randint(0, MAX_AXIS_VALUE), randint(0, MAX_AXIS_VALUE)) for _ in range(POINT_COUNT)]
cluster_centers = [Point(randint(0, MAX_AXIS_VALUE), randint(0, MAX_AXIS_VALUE)) for _ in range(CLUSTER_COUNT)]


def add_cluster_points_to_plot(cluster_points: list[Point]):
    x_coordinates = [p.x for p in cluster_points]
    y_coordinates = [p.y for p in cluster_points]
    plt.scatter(x_coordinates, y_coordinates)


def assign_points_to_cluster() -> None:
    for p in points:
        min_distance = sys.maxsize
        cluster_index = -1
        for i in range(CLUSTER_COUNT):
            dist = p.calc_distance(cluster_centers[i])
            if dist < min_distance:
                min_distance = dist
                cluster_index = i
            p.cluster_index = cluster_index


def display_all_clusters() -> None:
    for i in range(CLUSTER_COUNT):
        cluster_points = [p for p in points if p.cluster_index == i]
        add_cluster_points_to_plot(cluster_points)
    add_cluster_points_to_plot(cluster_centers)
    plt.show()


def update_cluster_centers() -> bool:
    cluster_centers_changed = False
    for i in range(CLUSTER_COUNT):
        cluster_points = [p for p in points if p.cluster_index == i]
        x_updated = round(sum([p.x for p in cluster_points]) / len(cluster_points))
        y_updated = round(sum([p.y for p in cluster_points]) / len(cluster_points))
        if cluster_centers[i].x != x_updated or cluster_centers[i].y != y_updated:
            cluster_centers_changed = True
            cluster_centers[i].x = x_updated
            cluster_centers[i].y = y_updated
    return cluster_centers_changed


if __name__ == "__main__":
    assign_points_to_cluster()
    while update_cluster_centers():
        assign_points_to_cluster()
        display_all_clusters()
