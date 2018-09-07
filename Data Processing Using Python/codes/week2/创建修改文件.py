# -*- coding: utf-8 -*-

'''
提示：可以利用list的insert函数
(1) 创建一个文件Blowing in the wind.txt，其内容是：
How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind
(2) 在文件头部插入歌名“Blowin’ in the wind”
(3) 在歌名后插入歌手名“Bob Dylan”
(4) 在文件末尾加上字符串“1962 by Warner Bros. Inc.”
(5) 在屏幕上打印文件内容
'''
lyrics = '''How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind'''

with open('Blowing in the wind.txt','w') as f:
    f.writelines(lyrics)
    
with open('Blowing in the wind.txt','r') as f:
    lyrics = f.readlines()
    lyrics.insert(0, "Blowin' in the wind\n")
    lyrics.insert(1, "Bob Dylan\n")
    
with open('Blowing in the wind.txt','w') as f:  
    f.writelines(lyrics)
    
with open('Blowing in the wind.txt','a') as f:
    f.write("\n1962 by Warner Bros. Inc.")
    

