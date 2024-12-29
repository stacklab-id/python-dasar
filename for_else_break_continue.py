
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("==========================")

for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i)

print("==========================")

for i in range(1, 6):
    print(i)
else:
    print("perulangan selesai!")
