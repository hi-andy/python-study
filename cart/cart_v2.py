#!/usr/bin/env python

# 提示用户输入可用金额
salary = int(input('Please input your salary: '))

# 读取商品列表
with open('goods', 'r') as goods:
    goods = goods.read()
goods_list = eval(goods)

# 读取已购商品列表
with open('bought_goods', 'r') as goods:
    goods = goods.read()
bought_list = eval(goods)
balance = bought_list['balance']
del bought_list['balance']

# 显示上次购买商品列表，和余额。
print('''Your bought goods are {_goods}'''.format(_goods=bought_list))
print('''Your balance is \033[31;1m{salary}\33[0m'''.format(salary=balance))


def show_goods_list(goods_input):
    print(' goods list '.title().center(50, '-'))

    for key in goods_input:
        print(key, goods_input[key])
    print('\r\n')


print('\r\n')
show_goods_list(goods_list)

goods_no = ''
cart = {}
goods_amount = 0

while True:
    # 提示用户输入要购买的商品名称
    goods_name = input('Please input you want to buy the name of goods:')
    if goods_name == 'q':
        break
    if goods_name in goods_list:
        # print(goods_name)
        if salary > int(goods_list[goods_name]):
            cart[goods_name] = goods_list[goods_name]
            print('''Your selected goods added into cart {_goods}'''.format(_goods=cart))
            show_goods_list(goods_list)

    else:
        print('You input goods name not exist, Please select other\n')
        show_goods_list(goods_list)


# 计算购物车中商品总金额
if len(cart) > 0:
    for k in cart:
        goods_amount += int(cart[k])
    # 用户余额减掉购买的商品金额 = 最终余额
    salary -= goods_amount
    cart['balance'] = salary
    with open('bought_goods', 'w') as goods:
        goods.write(str(cart))


# 显示结算详情：购买的商品，和最后余额。
print('''Your bought goods are {_goods}'''.format(_goods=cart))
print('''Your balance is \033[31;1m{salary}\33[0m'''.format(salary=salary))

