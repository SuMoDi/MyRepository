def get_shop_list():
    l = []
    with open(r'shop_list.txt','r') as f:
        for i in f.readlines():
            if i != '\n':
                i=i.rstrip('\n')
                i = i.split('\t')
                l.append(i[0])
                l.append(i[1])
        return l
        
shop_list = get_shop_list()

def show_shop_list(shop_list):
    for i in range(len(shop_list)):
        if i%2 == 0: 
          print ('thing: %s ' % (shop_list[i]),end='\t')
        else:
          print ('price: %s\n' % (shop_list[i]),end='')  

def jisuan(goods_list,shop_list):
    price = 0
    for i in goods_list:
        if i in shop_list:
           price += int(shop_list[shop_list.index(i)+1])
    return price
    

def shopping():
    salary = int(input('Please enter your salary:'))
    show_shop_list(shop_list)
    while True:
        goods = input('Please input the goods you want to buy:')
        goods_list = goods.split(',')
        price = jisuan(goods_list,shop_list)
        if price > salary:
            print ('Money is not enough')
            break
        else:
            salary -= price
            print (salary)
            flag = input('Continue？(y/n):')
            if flag[0].lower() == 'n':
                print ('shopping is over')
                break

shopping()
