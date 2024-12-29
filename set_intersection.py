
set_x = {1, 2, 3}
set_y = {1, 2, 'ok'}
set_z = {3, 4, 1}

print(set_x.intersection(set_y))
print(set_x.intersection(set_z))

print(set_x)

set_x.intersection_update(set_y)

print(set_x)

hasil = set_x & set_y

print(hasil)

