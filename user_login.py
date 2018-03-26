
name = input('user name:')
password = input('password')


PContent = []
LContent = []

with open('locked', 'r') as locked :
    lines = locked.readlines()

for line in lines:
    LContent.append(line.strip())

if name in LContent :
    print('Your account is locked! Bye!')
    exit()

with open('passwd', 'r') as passwd :
    lines = passwd.readlines()

for line in lines:
    PContent.append(line.strip())




for i in range(3):
    if name in PContent and password in PContent :
        print('welcome {name}, login success!'.format(name=name))
        break
    else :
        print('Name or Password error! Please retries')
        name = input('user name:')
        password = input('password')
else :
    with open('locked', 'w') as locked:
        locked.write(name)



#print(content)




# for i in range(3):
#     if name == correct_user and password == correct_pass:
#         print('welcome {name}'.format(name=name))
#     else:.
0#         print('Name or Password error!')41
#00 else:>{    print('You tried many times!')
