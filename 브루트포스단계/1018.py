N, M = map(int, input().split())
board = [input() for _ in range(N)]

answer = 64

for i in range(N-7):
    for j in range(M-7):
        W = 0
        B = 0
        
        for k in range(8):
            for l in range(8):
                color = board[i+k][j+l]
                if (k+l) % 2 == 0:
                    if color == 'B': W += 1
                    if color == 'W': B += 1
                else:
                    if color == 'W': W += 1
                    if color == 'B': B += 1
        
        answer = min(answer, W, B)

print(answer)