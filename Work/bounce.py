# bounce.py
#
# Exercise 1.5

count = 0
height = 100

while count < 10:
    count += 1
    height = round(height * 0.6, 4)
    print(count, height)

