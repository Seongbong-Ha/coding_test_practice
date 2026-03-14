import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
numbers = [int(x) for x in data[1:]]

numbers.sort()


print('\n'.join(map(str, numbers)))