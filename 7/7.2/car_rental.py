# 餐馆订位

have_dinner_number = input('请问有多少人用餐？\n')
have_dinner_number = int(have_dinner_number)
if have_dinner_number > 8:
    print('非常抱歉，暂时没有空桌了')
else:
    print('你好，还有空桌，这边请')
