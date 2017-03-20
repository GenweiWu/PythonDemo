# _*_ coding:utf-8 _*_
#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制

a = raw_input("a:")
n = int(raw_input("n:"))

sum=0
arr = []
for i in range(1,n+1):
	temp=int(a*i)
	arr.append(temp)
	sum=sum+temp

print "%d = %s" % (sum,' + '.join(str(i) for i in arr))


#output
# a:2
# n:4
# 2468 = 2 + 22 + 222 + 2222