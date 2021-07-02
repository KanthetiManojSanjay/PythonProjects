from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 2)
print(point.x)
print(point.y)

ThreeDPoint = namedtuple('ThreeDPoint', ['x', 'y', 'z'])
threeDpoint = ThreeDPoint(3, 4, 5)
print(threeDpoint.x)
print(threeDpoint.y)
print(threeDpoint.z)
