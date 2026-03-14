import sys

input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])

S = set(data[2:2+N])
words = data[2+N:]
cnt = 0

for w in words:
    if w in S:
        cnt += 1
    
            
print(cnt)