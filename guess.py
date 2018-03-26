

boy_age = 43

# 用户没有输入任何东西，直接按了回车？？？
# guess_age = input('guess age: ')
# guess_age = int(guess_age)
# while guess_age != boy_age :
#     if guess_age > boy_age:
#         guess_age = input('More smaller: ')
#     elif guess_age < boy_age :
#         guess_age = input('More bigger: ')
#     else:
#         guess_age = input('Please input age:')
#
# do : print('Yeh, congratulation!')


for i in range(3) :
    guess_age = int(input('Please input age:'))
    if guess_age == boy_age :
        print('Yeah, congratulation!')
        break
    if guess_age > boy_age:
        print('More smaller: ')
    else :
        print('More bigger: ')
else :
    print('You tried many times!')



