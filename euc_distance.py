points = [(1,2), (4,6), (5,8)]

import math
def euclideanDistance(point1, point2):
   return math.sqrt(( point1[0] - point2[0]) ** 2 + (point1[1]- point2[1])**2)
distance = euclideanDistance(points[0], points[1])
print(f"Noktalar arasındaki mesafe: {distance}")

distance =[]
for i in range (len(points)):
   for j in range (i + 1, len(points)):
      distance.append(euclideanDistance(points[i], points[j]))

min_distance = min(distance)
print(f"Minimum mesafe: {min_distance}")