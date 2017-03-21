# _*_ coding:utf-8 _*_
#猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，
#又多吃了一个。第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，
#见只剩下一个桃子了。求第一天共摘了多少。

def calculate(left):
    return 2*(left+1)
    
num=9

sum=1
while num > 0:
    sum = calculate(sum)
    print "[{}] ==> left before eat that day:{}".format(num,sum)
    pass
    num=num-1