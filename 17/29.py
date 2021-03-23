a, b = 2807, 8558 + 1

mx = 0
sm = 0

for i in range(a, b):
    if i // 2 % 2 == 1 and i % 2 == 1 and i % 9 ==5:
        sm += i
        mx = max(mx, i)

print(sm, mx)


