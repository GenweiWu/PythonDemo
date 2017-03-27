# _*_ coding:utf-8 _*_
# 练习函数调用。


def hello(name):
	print "hello",name
	pass

def manyHello():
	for i in ["a","bobo","green"]:
		hello(i)
	pass	

manyHello()	