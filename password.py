import getpass

name = input('user name:')
#password = getpass.getpass('password')
password = input('password')


correct_user = 'hua'
correct_pass = '123'

if name == correct_user and password == correct_pass :
    print('welcome {name}'.format(name=name))

else:
    print('error')
