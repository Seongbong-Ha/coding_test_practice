import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
points = []

index = 1
for i in range(N):
    x = int(data[index])
    y = int(data[index + 1])
    points.append((x, y))
    index += 2

points.sort()

for x, y in points:
    print(x, y)