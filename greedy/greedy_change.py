n = int(input())
coin = [500, 100, 50, 10]
acc = 0
for i in coin:
    acc += n // i
    n %= i
print(acc)
