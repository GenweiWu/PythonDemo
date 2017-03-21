# _*_ coding:utf-8 _*_
#打印出如下图案（菱形）:
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *

# for i in [1,3,5,7,5,3,1]:
#   left = (7 - i)/2
#   print left*' ',i*'*'


#自我提升下，通过输入的n(标识打印最多的行的*的个数/必须是奇数)来打印
import sys

num = int(raw_input("n="))
if num<0 or num%2==0:
    print "error num."
    sys.exit(0)


index=1
arr=[]

#1,3,5,7
while index<=num:
    arr.append(index)
    index=index+2 
#5,3,1
index=num
index=index-2
while index>=1:
    arr.append(index)
    index=index-2 

#print arr
for i in arr:
    left = (num - i)/2
    print left*' ',i*'*'


 #output:
 #n=13
 #       *
 #      ***
 #     *****
 #    *******
 #   *********
 #  ***********
 # *************
 #  ***********
 #   *********
 #    *******
 #     *****
 #      ***
 #       *    