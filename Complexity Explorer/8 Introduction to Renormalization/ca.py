# coarse-graining cellular automata
# a worked example of the Israeli & Goldenfeld procedure
# https://journals.aps.org/pre/abstract/10.1103/PhysRevE.73.026203
# for the SFI Renormalization MOOC
# http://renorm.complexityexplorer.org
# Simon DeDeo / simon@santafe.edu / http://santafe.edu/~simon

import string

def rule_expansion(rule_number):
	ans=('{0:b}'.format(rule_number).rjust(8, '0'))[::-1]
	return ans
## the rule is just the binary expansion of the rule_number (don't forget to left-pad with zeros)
## note funny Wolfram definitions mean we have to reverse the sequence

def f(triplet, rule):
	return rule[int(triplet,2)]
# how to access the output of a rule given a triplet value; e.g., black-white-black is 2; the third entry in the Wolfram binary expansion

def f2(sextet, rule):
	A=f(f(sextet[0:3], rule)+f(sextet[1:4], rule)+f(sextet[2:5], rule), rule)
	B=f(f(sextet[1:4], rule)+f(sextet[2:5], rule)+f(sextet[3:6], rule), rule)
	return A+B
# the two step case, exact

def proj(super_cell, rule):
	return rule[int(super_cell,2)]

rule105=rule_expansion(105)
rule150=rule_expansion(150)
proj_rule='0110' # the "edge detection" coarse-graining
# if it is 00 [first entry in lookup], then 0; 01 [second entry in lookup], then 1; 10 [third entry in lookup], then 1; 11 [last entry in lookup], then 2

tests=[]
for sextet in ['{0:b}'.format(i).rjust(6, '0') for i in range(2**6)]:
	tests.append([proj(f2(sextet,rule105),proj_rule), f(proj(sextet[0:2],proj_rule)+proj(sextet[2:4],proj_rule)+proj(sextet[4:6],proj_rule),rule150)])
	if tests[-1][0] != tests[-1][1]:
		print('Coarse-graining relationship fail at '+str(sextet))
## no flags raised; all tests passed -- implies rule105 coarse-grains to rule150

## another test, from Sec III.A of https://arxiv.org/pdf/nlin/0508033.pdf
rule128=rule_expansion(128)
tests=[]
proj_rule='0111'
for sextet in ['{0:b}'.format(i).rjust(6, '0') for i in range(2**6)]:
	tests.append([proj(f2(sextet,rule128),proj_rule), f(proj(sextet[0:2],proj_rule)+proj(sextet[2:4],proj_rule)+proj(sextet[4:6],proj_rule),rule128)])

## now cycle through all non-trivial coarse-grainings for rule 105->150 map
for proj_rule in ['{0:b}'.format(i).rjust(4, '0') for i in range(1,2**4-1)]:
	tests=[]
	ok=True
	for sextet in ['{0:b}'.format(i).rjust(6, '0') for i in range(2**6)]:
		tests.append([proj(f2(sextet,rule105),proj_rule), f(proj(sextet[0:2],proj_rule)+proj(sextet[2:4],proj_rule)+proj(sextet[4:6],proj_rule),rule150)])
		if tests[-1][0] != tests[-1][1]:
			ok=False
	if ok:
		print('Valid coarse-graining for 105->150: '+str(proj_rule))


	
