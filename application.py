# def chebyshev_distance(p1, p2):
#     """Docstring..."""
#     return max(abs(x - y) for x, y in zip(p1, p2))

# if __name__ == "__main__":
#     point1 = (1, 2, 3)
#     point2 = (4, 5, 6)
#     distance = chebyshev_distance(point1, point2)
#     print("Chebyshev Distance:", distance)


def chebyshev_distance_way1(p1, p2):
    """Calculate the Chebyshev distance between two points."""
    max_diff = 0
    for x, y in zip(p1, p2):
        max_diff = max(max_diff, abs(x - y))
    return max_diff

if __name__ == "__main__":
    point1 = (1, 2, 3)
    point2 = (4, 5, 6)
    distance = chebyshev_distance_way1(point1, point2)
    print("Chebyshev Distance:", distance)

