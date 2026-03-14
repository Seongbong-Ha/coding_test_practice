import sys

N = input()

mylist = list(N)
mylist.sort(reverse = True)

print(''.join(map(str, mylist)))