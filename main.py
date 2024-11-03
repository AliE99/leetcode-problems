x = 19

res = 0
for i in str(x):
    res += int(i) * int(i)

print(res)

while True:
    x = res
    res = 0
    for i in str(x):
        res += int(i) * int(i)
    if res == 1:
        print("asdasd")
