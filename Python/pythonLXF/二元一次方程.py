# -*- coding: utf-8 -*-
import math
def my_quadratic(a,b,c):
	if not isinstance(a,(int,float)) or isinstance(b,(int,float)) or isinstance(c,(int,float)):
		raise TypeError('请输入正确的数值！')
	elif b**2 - 4*a*c < 0 or (a==0 and b==0):
		return '此方式无解！'
	x1=(-b+math.sqrt(b**2 - 4*a*c))/2*a
	x2=(-b-math.sqrt(b**2 - 4*a*c))/2*a
	#return x1,x2
	return '方程的解分别为X1=%.3f，X2=%.3f。'%(x1,x2)