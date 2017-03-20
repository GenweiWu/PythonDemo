# _*_ coding:utf-8 _*_
# 一个数如果恰好等于除它本身外的因子之和，这个数就称为"完数"。
# 例如6=1＋2＋3.编程找出1000以内的所有完数。

#这题
import math

def getFactor(num):
	arr=[]
	target = int(math.floor(math.sqrt(num)))

	arr.append(1)
	for i in range(2,target+1):
		if num%i==0:
			j = num/i
			arr.append(i)
			if j!=i:
				arr.append(j)


	return arr	
	pass

#1不符合，直接跳过了
for j in range(2,1001):
	factor = getFactor(j)
	factor.sort()
	if j == sum(factor):
		print "%d = %s" % (j,'+'.join(str(k) for k in factor))

#output:
# 6 = 1+2+3
# 28 = 1+2+4+7+14
# 496 = 1+2+4+8+16+31+62+124+248