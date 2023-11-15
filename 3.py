a = [int(i) for i in input().split()]
a.sort()
for i in range(len(a)-1):
    if i == len(a)-2 or a[i + 1] != a[i + 2]:
        if a[i] == a[i + 1]:
            print(a[i], end=" ")