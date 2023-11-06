
#图形化界面
from turtle import *

# #设置笔刷宽度
# width(4)

# #前进
# forward(200)
# #右转90度：
# right(90)

# #笔刷颜色
# pencolor('red')

# forward(100)
# right(90)

# pencolor('green')
# forward(200)
# right(90)

# pencolor('blue')
# forward(100)
# right(90)

# done()


def drawStar(x,y):
    pu()
    goto(x,y)
    pd()
    
    #set heading:0
    seth(0)
    for i in range(6):
        fd(60)
        rt(60)
        
for x in range(-450,450,150):
    drawStar(x,0)
    
done()