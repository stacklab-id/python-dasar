set_a = {'google', 'facebook', 'instagram'}
set_b = {'youtube', 'facebook', 'instagram'}

set_c = set_a.symmetric_difference(set_b)
set_d = set_a ^ set_b

print(set_c)
print(set_d)

print(set_a)

set_a.symmetric_difference_update(set_b)
print(set_a)


