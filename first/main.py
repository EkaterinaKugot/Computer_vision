# Nominal resolution

for i in range(1, 7):
    f = open(f"figure{i}.txt", "r")
    size_obj = float(f.readline())
    f.readline()

    max_len = 0

    for line in f:
        photo_len = list(map(int, line.split()))
        number_one = photo_len.count(1)

        if (max_len < number_one):
            max_len = number_one

    f.close()

    if max_len == 0:
        result = 0
    else:
        result = float(size_obj / max_len)

    print(f"Nominal resolution for figure{i}: {result} mm")

# Determine the offset

x1, y1 = 0, 0
for k in range(1, 3):   
    with open(f"img{k}.txt") as f:
        img = f.readlines()
        img.pop(0)
        img.pop(0)
        img = [list(map(int, i.split())) for i in img]
        y, x = 0, 0
        for i in img:
            if 1 in i:
                y = img.index(i)
                x = i.index(1)
                break
    if (x1 != 0 and y1 != 0):
        x1 = x - x1
        y1 = y - y1
    else:
        x1, y1 = x, y
    
print(f"\nOffset by y = {y1}, x = {x1}")



