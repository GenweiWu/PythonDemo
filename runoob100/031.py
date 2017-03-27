# _*_ coding:utf-8 _*_
# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# monday tuesday wednesday thursday friday saturday sunday

i = raw_input("please input:")
i = i.upper()
if i=="M":
    print "Monday" 
elif i=="T":
    print "Tuesday" 
elif i=="W":
    print "Wednesday"
elif i=="T":
    print "Thursday"
elif i=="F":
    print "Friday"
elif i=="S":
    j = raw_input("please input second:")
    j = j.upper()
    if j=="A":
        print "Saturday"
    elif j=="U":
        print "Sunday"
