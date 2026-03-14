import sys

N = int(input())
answer = 665
mylist = []

while len(mylist) < N:
    answer += 1
    if '666' in str(answer):
        mylist.append(answer)

print(mylist[N-1])