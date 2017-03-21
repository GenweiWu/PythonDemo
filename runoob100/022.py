# _*_ coding:utf-8 _*_
#两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
#已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，
#请编程序找出三队赛手的名单。


#假设abc已经站在那儿了，就是xyz的组合了呀

for i in ['x','y','z']:
	for j in ['x','y','z']:
		for k in ['x','y','z']:
			if i!=j and i!=k and j!=k:
				if i!='x' and k!='x' and k!='z':
					print "a-{} b-{} c-{}".format(i,j,k)