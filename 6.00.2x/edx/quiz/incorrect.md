## Problem 2-1

Which of the following problems can be solved using dynamic programming? Check all that work.

Sum of elements - Given a list of integer elements, find the sum of all the elements. 

Binary search - Given a list of elements, check if the element X is in the list. 

Dice throws - Given n dice each with m faces, numbered from 1 to m, find the number of ways to get sum X. X is the summation of values on each face when all the dice are thrown.



Optimal substructure and Overlapping subproblems are required for dynamic programming.

I think answer is "Dice throws". Binary search doesn't have overlapping subproblems.



## Problem 2-2

What is the exact probability of rolling at least two 6's when rolling a die three times?
$$
C_3^2 \times \frac{1}{6} \times \frac{1}{6} \times \frac{5}{6} + \frac{1}{6} \times \frac{1}{6} \times \frac{1}{6} = \frac{2}{27}
$$
1/6 * 1/6 is rolling two 6's when rolling a die two times.



##  Problem 7-3

```python
nodes = []
for i in range(n):
    nodes.append(newNode(i)) # newNode takes one parameter, the number of the node

for i in range(len(nodes)):
	w = random.choice(nodes)
	x = random.choice(nodes)
	y = random.choice(nodes)
	z = random.choice(nodes)
	addEdge(w,x)
	addEdge(x,y)
	addEdge(y,z)
	addEdge(z,w)	
```

loop or connected chain of nodes  incorrect