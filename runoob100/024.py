# _*_ coding:utf-8 _*_
#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

num=20/2

arr=[]

#first get: [1,2,3,5,8...]
i=1.0
j=2.0
arr.append(i)
arr.append(j)

while num>0:
	i=i+j
	j=i+j
	arr.append(i)
	arr.append(j)
	pass
	num=num-1

#then get dataArr
dataArr=[]
for i in range(0,20):
	data = arr[i+1]/arr[i]
	#print "{}/{}={}".format(arr[i+1],arr[i],data)
	dataArr.append(data)	

print sum(dataArr)