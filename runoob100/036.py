# _*_ coding:utf-8 _*_
# 求100之内的素数。


def primeNumber(num):
	if num==1:
	    return False
	if num==2:
		return True
	for i in range(2,num):
		if num%i==0:
			return False
	return True


for i in range(1,101):
	if primeNumber(i):
		print i