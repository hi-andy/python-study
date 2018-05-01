def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


extra = {'city': 'BJ', 'job': 'Engineer'}
cp_extra = extra
print(person('Micheal', 30, **extra))
print(cp_extra)
