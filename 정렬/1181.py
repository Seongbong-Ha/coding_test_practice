import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
mylist = data[1:]

unique_word = list(set(mylist))
unique_word.sort(key=lambda x: (len(x), x))

for word in unique_word:
    print(word)