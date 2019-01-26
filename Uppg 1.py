sum = 0
x = 0
y = 0
count = 1000
while x <= count:
    sum += x
    x += 3
while y <= count:
    if y % 3 != 0 and y < count:
        sum += y
    y += 5
print(sum)
