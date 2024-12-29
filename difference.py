
set_a = {1, 2, 3}
set_b = {1, 2, 4}
set_c = {2, 5, 3}

print(set_a.difference(set_b))

print(set_a - set_c)

print(set_a)

set_a.difference_update(set_b)

print(set_a)