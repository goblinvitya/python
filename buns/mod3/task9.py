step = int(input())
x = 0
y = 0
dx, dy = 0, -1

for i in range(step):
    if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
        dx, dy = -dy, dx
    x, y = x+dx, y+dy
print(-x, -y)