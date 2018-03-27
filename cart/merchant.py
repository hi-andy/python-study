#!/usr/bin/env python

# 读取商品列表
with open('goods', 'r') as goods:
    goods = goods.read()
goods_list = eval(goods)


for key in goods_list:
    print(key, goods_list[key])

exit_code = "q"
# 添加或修改商品价格
while True:
    goods_name = input('input goods name or exit input q:')
    if goods_name == exit_code:
        break
    goods_price = input('input goods price:')
    if not goods_price.isdigit():
        goods_price = input('input goods price is number:')
    else:
        goods_list[goods_name] = goods_price

goodsStr = str(goods_list)

if len(goods_list) > 0:
    with open('goods', 'w') as goods:
        goods.write(goodsStr)
