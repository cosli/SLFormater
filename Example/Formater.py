"""这是用于将surfer散点加载至landmark中的Python3脚本，仅需指定组名至第31行Zu=[]中即可，如Zu=["T52","T53"]"""
import os

#定义格式化函数
def formater(filename=[]):
	for file in filename:
		print(file,end=' ')
		print(filename.index(file)+1)
	#构造X与Y
		with open(file,"r") as data:
			X=[]
			Y=[]
			for line in data:
				(x,y)=line.split(",",2)
				X.append(x)
				Y.append(y)
	#构造Z
		Z=[0]
		Z.append(6)
		for i in range(len(X)-3):
			Z.append(7)
		Z.append(8)
	#格式化输出
		with open(file+".out","w") as out:
			for i in range(1,len(X)):
				print('%.3f' % float(X[i]),end=' ',file=out)
				print('%.3f' % float(Y[i])+"999999999999",end='  ',file=out)
				print(Z[i],end='    ',file=out)
				print(filename.index(file)+1,file=out)
#########在这里指定#########
Zu=["T1","T2"]
##########################
#依次生成指定组文件名列表
for Tnum in Zu:
	cmd="ls "+Tnum+"*.bln"+">"+"lists"
	os.system(cmd)
	#读入当前组文件名列表
	with open("lists") as lists:
		filename=[]
		for line in lists:
			filename.append(line.strip('\n'))
		os.system('rm -f lists')
		formater(filename)
	#将零散文件结合到一起并删除过程文件
	join="cat "+Tnum+"*.out"+">"+Tnum+".dat"
	dele="rm -f "+Tnum+"*.out"
	os.system(join)
	os.system(dele)