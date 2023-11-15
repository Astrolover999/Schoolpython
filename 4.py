a = []
b = int(input())
c = 0
for i in range(1, b+1):
    c = min(b, i)
    b = b - c
    a += [str(i)] * c
    if b <= 0:
        break
print(" ".join(a))