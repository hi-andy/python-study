#!/usr/bin/env python

# 提示用户输入可用金额
salary = int(input('Please input your salary: '))

# 商品列表
goods_list = [['IPhone', 5800], ['Mac Pro', 14000], ['Book', 18], ['Bicycle', 12000]]


def show_goods_list(goods_input):
    print(' goods list '.title().center(50, '-'))

    # for i in goods_list:
    #     print(''' {_i}. {goods} '''.format(_i=goods_list.index(i)+1, goods=i))

    # 显示商品列表
    # 改进版：使用 enumerate 类似 PHP 中的 foreach
    for key, value in enumerate(goods_input):
        print(''' {_i}. {goods} '''.format(_i=key + 1, goods=value))


show_goods_list(goods_list)

goods_no = ''
cart = []
goods_amount = 0

while goods_no != 'q':
    # 提示用户输入要购买的商品编号
    goods_no = input('Please select you want to buy the number of goods:')
    if goods_no.isdigit():
        goods_no = int(goods_no) - 1
        if len(goods_list) > goods_no >= 0:
            goods = goods_list[goods_no]
            if salary > int(goods[1]):
                cart.append(goods)
                print('''Your selected goods added into cart {_goods}'''.format(_goods=cart))
                show_goods_list(goods_list)
else:
    # 计算购物车中商品总金额
    for i in cart:
        goods_amount += int(i[1])

# 用户余额减掉购买的商品金额 = 最终余额
salary -= goods_amount

# 显示结算详情：购买的商品，和最后余额。
print('''Your bought goods are {_goods}'''.format(_goods=cart))
print('''Your balance is \033[31;1m{salary}\33[0m'''.format(salary=salary))

