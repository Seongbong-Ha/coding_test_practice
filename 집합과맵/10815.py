import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
cards = set(data[1:1+N])

M = int(data[1+N])
answer = data[1+N+1:]

result = []

for i in answer:
    if i in cards:
        result.append('1')
    else:
        result.append('0')
        
print(' '.join(result))