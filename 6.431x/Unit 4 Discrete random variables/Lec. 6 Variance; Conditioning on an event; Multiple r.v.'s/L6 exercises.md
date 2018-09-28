## 3. Exercise: Variance calculation

Suppose that Var(X)=2. The variance of 2−3X is:

Var(2−3X)=



**Solution:**

The random variable 2−3X is of the form aX+b, with a=−3 and b=2. Thus, Var(2−3X)=(−3)2Var(X)=9⋅2=18.



## 4. Exercise: Variance properties

Is it always true that $E[X^2]≥(E[X])^2$ ?

We know that variances are always nonnegative and that Var(X)=E[X^2]−(E[X])^2. Therefore, 0≤Var(X)=E[X^2]−(E[X])^2, or, equivalently, E[X^2]≥(E[X])^2.



## 6. Exercise: Variance of the uniform



Suppose that the random variable X takes values in the set {0,2,4,6,…,2n} (the even integers between 0 and 2n, inclusive), with each value having the same probability. What is the variance of X? *Hint:* Consider the random variable Y=X/2 and recall that the variance of a uniform random variable on the set {0,1,…,n} is equal to n(n+2)/12.

Var(X)=

**Solution:**

Following the hint, let Y=X/2. The random variable Y takes values in the set {0,1,2,…,n}, each value having the same probability. Therefore, Y is uniform and has a variance of n(n+2)/12. Since X=2Y,
$$
\textsf{Var}(X)=\textsf{Var}(2Y)=4\cdot \textsf{Var}(Y)=\frac{4}{12}n(n+2).
$$


## 8. Exercise: Conditional variance



In the last example, we saw that the conditional distribution of X, which was a uniform over a smaller range (and in some sense, less uncertain), had a smaller variance, i.e., Var(X∣A)≤Var(X). Here is an example where this is not true. Let Y be uniform on {0,1,2} and let B be the event that Y belongs to {0,2}.

a) What is the variance of Y?

Var(Y)=



b) What is the conditional variance Var(Y∣B)?

Var(Y∣B)=

 

**Solution:**

a) The calculation of the variance of Y is exactly the same as the calculation of Var(X∣A) in the preceding example, yielding 2/3.

b) In the conditional model, the conditional mean is E[Y∣B]=1. Since Y is either 0 or 2 in the conditional model, the difference between Yand the conditional mean is either 1 or −1, so that (Y−E[Y∣B])2 is always equal to 1. It follows that the conditional variance is equal to 1.

Note that in this example, Var(Y∣B)>Var(Y).



## 11. Exercise: Total expectation calculation

We have two coins, A and B. For each toss of coin A, we obtain Heads with probability 1/2; for each toss of coin B, we obtain Heads with probability 1/3. All tosses of the same coin are independent. We select a coin at random, where the probabilty of selecting coin A is 1/4, and then toss it until Heads is obtained for the first time.



The expected number of tosses until the first Heads is:  



**Solution:**

Let T be the number of tosses until the first Heads. Once a coin is selected, the conditional distribution of T is geometric, with a mean of 1/p, where p is the probability of Heads for the selected coin. Let CA and CB denote the events that coin A or B, respectively, is selected.
$$
{\bf E}[T]={\bf P}(C_ A) {\bf E}[T\mid C_ A]+{\bf P}(C_ B){\bf E}[T\mid C_ B]=\frac{1}{4}\cdot 2 +\frac{3}{4}\cdot 3=\frac{11}{4}.
$$


## 12. Exercise: Memorylessness of the geometric

### Exercise: Memorylessness of the geometric

2/2 points (graded)



Let X be a geometric random variable, and assume that Var(X)=5.

a) What is the conditional variance Var(X−4∣X>4)?

Var(X−4∣X>4)=



b) What is the conditional variance Var(X−8∣X>4)?

Var(X−8∣X>4)=

   

**Solution:**

a) The conditional distribution of X−4 given X>4 is the same geometric PMF that describes the distribution of X. Hence Var(X−4∣X>4)=Var(X)=5.

b) In the conditional model (i.e., given that X>4), the random variables X−4 and X−8 differ by a constant. Hence they have the same variance and the answer is again 5.





## 14. Exercise: Joint PMF calculation

The random variable V takes values in the set {0,1} and the random variable W takes values in the set {0,1,2}. Their joint PMF is of the form
$$
p_{V,W}(v,w)=c\cdot (v+w)
$$


where c is some constant, for v and w in their respective ranges, and is zero everywhere else.

a) Find the value of c.

c=

 .





b) Find pV(1).

pV(1)=

 **Solution:**

a) The sum of the entries of the PMF is c⋅(0+0)+c⋅(0+1)+c⋅(0+2)+c⋅(1+0)+…=9c. Since this sum must be equal to 1, we have c=1/9.

b)
$$
p_ V(1)=\sum _{w=0}^2 p_{V,W}(1,w)= p_{V,W}(1,0)+p_{V,W}(1,1)+p_{V,W}(1,2) =\frac{1}{9}(1+2+3)=\frac{6}{9}.
$$

# impotant

Let X and Y be discrete random variables. For each one of the formulas below, state whether it is true or false.

a).
$$
{\bf E}[X^2]=\sum _ x x p_ X(x^2)
$$
b).
$$
{\bf E}[X^2]=\sum _ x x^2 p_ X(x)
$$
c).
$$
{\bf E}[X^2]=\sum _ x x^2 p_{X,Y}(x)
$$
d).
$$
{\bf E}[X^2]=\sum _ x x^2 p_{X,Y}(x,y)
$$
e).
$$
{\bf E}[X^2]=\sum _ x\sum _ y x^2 p_{X,Y}(x,y)
$$
f).
$$
{\bf E}[X^2]=\sum _ z z p_{X^2}(z)
$$
**Solution:**

a) False. This does not follow from any of our formulas.

b) True. This is the expected value rule for a function of a single random variable.

c) False. This is syntactically wrong since the function $pX,Y$ needs two arguments.

d) False. The left-hand side is a number whereas the right-hand side is actually a **function of y**.

e) True. This is the expected value rule
$$
{\bf E}[g(X,Y)]=\sum _ x \sum _ y g(x,y) p_{X,Y}(x,y),
$$
for the function g(x,y)=x^2.

f) True. This is just the definition of the expectation $E[Z]=∑zzpZ(z)$, where Z is the random variable X^2.



## 17. Exercise: Linearity of expectations drill

Suppose that E[Xi]=i for every i. Then,

E[X1+2X2−3X3]= -4



## 18. Exercise: Using linearity of expectations

We have two coins, A and B. For each toss of coin A, we obtain Heads with probability 1/2; for each toss of coin B, we obtain Heads with probability 1/3. All tosses of the same coin are independent.

We toss coin A until Heads is obtained for the first time. We then toss coin B until Heads is obtained for the first time with coin B.



The expected value of the total number of tosses is:  



**Solution:**

Let TA and TB be the number of tosses of coins A and B, respectively. We know that TA is geometric with parameter p=1/2, so that E[TA]=1/p=1/(1/2)=2. Similarly, E[TB]=3. The total number of coin tosses is TA+TB. Using linearity,
$$
{\bf E}[T_ A+T_ B]={\bf E}[T_ A]+{\bf E}[T_ B]=2+3=5.
$$






 





 