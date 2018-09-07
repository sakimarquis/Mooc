# -*- coding: utf-8 -*-

'''
有一个咖啡列表['32Latte', '_Americano30', '/34Cappuccino', 
'Mocha35']，列表中每一个元素都是由咖啡名称、价格和一些其他
非字母字符组成，编写一个函数clean_list()处理此咖啡列表，处
理后列表中只含咖啡名称，并将此列表返回。__main__模块中初始
化咖啡列表，调用clean_list()函数获得处理后的咖啡列表，并利
用zip()函数给咖啡名称进行编号后输出，输出形式如下：
1 Latte
2 Americano
3 Cappuccino
4 Mocha
'''

def clean_list(l):
    count = 0
    for i in l:
        l[count] =''.join(filter(str.isalpha,i))
        count += 1
    return l

def output(l):
    l = clean_list(l)
    for i,j in (zip(range(len(l)),l)):
        print(i+1,j)

#也可以用enumerate
def output1(l):
    l = clean_list(l)
    for i,j in enumerate(l):
        print(i+1,j)
        
coffee_list = ['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']  
output(coffee_list) 

output1(coffee_list)
                

