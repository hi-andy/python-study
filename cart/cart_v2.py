#!/usr/bin/env python

# 提示用户输入可用金额
salary = int(input('Please input your salary: '))

# 读取商品列表
with open('goods', 'r') as goods:
    goods = goods.read()
goods_list = eval(goods)

def show_goods_list(goods_input):
    print(' goods list '.title().center(50, '-'))

    for key in goods_input:
        print(key, goods_input[key])


show_goods_list(goods_list)

goods_no = ''
cart = {}
goods_amount = 0

while goods_no != 'q':
    # 提示用户输入要购买的商品编号
    goods_no = input('Please select you want to buy the number of goods:')
    if goods_no.isdigit():
        goods_no = int(goods_no)
        if len(goods_list) > goods_no >= 0:
            goods_name = list(goods_list[goods_no])[0]
            # print(goods_name)
            if salary > int(goods_list[goods_no][goods_name]):
                cart[goods_name] = goods_list[goods_no][goods_name]
                print('''Your selected goods added into cart {_goods}'''.format(_goods=cart))
                # TODO record bought goods list
                show_goods_list(goods_list)
else:
    # 计算购物车中商品总金额
    for key in cart:
        goods_amount += int(cart[key])

# 用户余额减掉购买的商品金额 = 最终余额
salary -= goods_amount

# TODO record user balance

# 显示结算详情：购买的商品，和最后余额。
print('''Your bought goods are {_goods}'''.format(_goods=cart))
print('''Your balance is \033[31;1m{salary}\33[0m'''.format(salary=salary))

