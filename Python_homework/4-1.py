#1 百元买百鸡
#用100元钱买100只鸡，母鸡每只3元，公鸡每只2元，小鸡一元3只，且每种鸡至少买一种，编程列出所有可能的购买方案 
for x in range(1,34):
    for y in range(1,50):
        if 3*x+2*y+(100-x-y)/3==100:print("母鸡",x,"只，公鸡",y,"只，小鸡",100-x-y,"只")
