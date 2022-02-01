from random import randint
import sys
from itertools import combinations

import matplotlib.pyplot as plt

from point import Point

MAX_AXIS_VALUE = 100
POINT_COUNT = 5000
points = [Point(randint(0, MAX_AXIS_VALUE), randint(0, MAX_AXIS_VALUE)) for _ in range(POINT_COUNT)]
cluster_centers = []


def assign_points_to_cluster() -> None:
    for p in points:
        min_distance = sys.maxsize
        cluster_index = -1
        for i in range(len(cluster_centers)):
            dist = p.calc_distance(cluster_centers[i])
            if dist < min_distance:
                min_distance = dist
                cluster_index = i
            p.cluster_index = cluster_index


def add_cluster_points_to_plot(cluster_points: list[Point]) -> None:
    x_coordinates = [p.x for p in cluster_points]
    y_coordinates = [p.y for p in cluster_points]
    plt.scatter(x_coordinates, y_coordinates)


def display_all_clusters() -> None:
    for i in range(len(cluster_centers)):
        cluster_points = [p for p in points if p.cluster_index == i]
        add_cluster_points_to_plot(cluster_points)
    add_cluster_points_to_plot(cluster_centers)
    plt.show()


def find_farthest_point(point, points_to_search):
    max_distance = -1
    res = points_to_search[0]
    for p in points_to_search:
        current_distance = p.calc_distance(point)
        if current_distance > max_distance:
            max_distance = current_distance
            res = p
    return res, max_distance


def calc_threshold():
    dist_sum = 0
    count = 0
    for pair in combinations(cluster_centers, 2):
        dist_sum += pair[0].calc_distance(pair[1])
        count += 1
    return dist_sum / count / 2


def find_cluster_center_candidate():
    cluster_farthest_points = []
    for i in range(len(cluster_centers)):
        cluster_points = [p for p in points if p.cluster_index == i]
        point_dist = find_farthest_point(cluster_centers[i], cluster_points)
        cluster_farthest_points.append(point_dist)
    max_dist = -1
    res_point = Point()
    for point, dist in cluster_farthest_points:
        if dist > max_dist:
            max_dist = dist
            res_point = point
    return res_point, max_dist


if __name__ == "__main__":
    first_center = points[0]
    second_center = find_farthest_point(first_center, points)[0]
    cluster_centers = [first_center, second_center]
    assign_points_to_cluster()

    while True:
        candidate, dist = find_cluster_center_candidate()
        threshold = calc_threshold()
        if dist <= threshold:
            break
        cluster_centers.append(candidate)
        assign_points_to_cluster()
    display_all_clusters()
