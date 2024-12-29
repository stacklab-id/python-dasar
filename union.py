
set_A = {1, 2, 3}
set_B = {4, 5, 6}

set_c = set_A.union(set_B)

print(set_c)

set_d = {7, 8, 9}
set_e = {11, 12, 13}

set_f = set_d | set_e

print(set_f)

x = {'a', 'b', 'c'}
y = {'d', 'e', 'f'}
z = {'g', 'h', 'i'}

# result = x.union(y, z)
result = x | y | z

print(result)