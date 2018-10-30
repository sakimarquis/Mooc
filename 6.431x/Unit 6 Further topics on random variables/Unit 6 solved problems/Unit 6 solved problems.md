

## 1. The PDF of the absolute value of X

**The PDF of |X|.** Let X be a random variable with PDF fX. Find the PDF of the random variable Y=|X|

1. When $\displaystyle f_ X(x) \  = \  \left\{  \begin{array}{ll} 1/3, &  \mbox{if $-2 < x \leq 1$}, \\ 0, &  \mbox{otherwise}; \end{array} \right.$

2. When $\displaystyle f_ X(x) \  = \  \left\{  \begin{array}{ll} 2e^{-2x}, &  \mbox{if $x > 0$}, \\ 0, &  \mbox{otherwise}; \end{array} \right.$
3. for general $f_X(x)$.



## 2. Derived distribution example

**Derived distribution example.** Let X have the normal distribution with mean 0 and variance 1, i.e.,
$$
f_ X(x) \  = \  \frac{1}{\sqrt{2\pi }} e^{-x^2/2}.
$$
Also, let Y=g(X) where
$$
\displaystyle g(t) \  = \  \left\{  \begin{array}{ll} -t, &  \mbox{for $t \leq 0$}; \\ \sqrt{t}, &  \mbox{for $t > 0$}, \end{array} \right.
$$
as shown below.

![The figure is the graph of a function defined on t. The x axis represents values of t and covers values of t ranging from -5 to 5 and has markings at t=-5, t=0, t=5, while the y axis represents values of f(D:\Study\Mooc\6.431x\Unit 6 Further topics on random variables\Unit 6 solved problems\images_4_1_derived_3_01.jpg) covering values of f(t) ranging from 0 to 5 and has markings at each unit. g(t) is a piecewise differentiable function in t that is not differentiable only at t=0. The left half of the graph shows a straight line sloping downwards, connecting (-5, 5) and (0, 0), while the right half of the graph is a concave, increasing curve that initially increases quickly then levels off, approaching a linear function towards the end of the part of the graph shown. In particular, the curve, representing the value of g(t)=sqrt(t) as t ranges from 0 to 5, from (0, 0) to approximately (5, 2.25). ](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/a25a147f963219ad0c0d07067c4453ed/asset-v1:MITx+6.431x+3T2018+type@asset+block/images_4_1_derived_3_01.jpg)



Find the probability density function of Y.



## 3. Ambulance travel time

**Ambulance travel time.** An ambulance travels back and forth, at a constant speed v, along a road of length ℓ. We may model the location of the ambulance at any moment in time to be uniformly distributed over the interval (0,ℓ). Also at any moment in time, an accident (not involving the ambulance itself) occurs at a point uniformly distributed on the road; that is, the accident's distance from one of the fixed ends of the road is also uniformly distributed over the interval (0,ℓ). Assume the location of the accident and the location of the ambulance are independent.

Supposing the ambulance is capable of **immediate** U-turns, compute the CDF and PDF of the ambulance's travel time T to the location of the accident.



## 4. The difference of two independent exponential r.v.'s

**The difference of two independent exponential random variables.** Romeo and Juliet have a date at a given time, and each, independently, will be late by an amount of time that is exponentially distributed with parameter λ. What is the PDF of the difference between their times of arrival?



For a written solution, see Example 4.12 on p. 216 of the text.

 in the case z>0, we still have the following definition of the convolution:
$$
f_Z(z)=\int_{-\infty}^{+\infty}f_X(x)f_Y(x-z)dx
$$
But fX(x)=0 when x<0 and fY(x−z)=0 when x−z<0. Therefore the product fX(x)fY(x−z) is equal to 0 when x<z, since z>0. And the convolution integral reduces to:
$$
f_Z(z)=\int_{z}^{+\infty}f_X(x)f_Y(x-z)dx=\int_{z}^{+\infty}\lambda^2e^{-\lambda x}e^{-\lambda (x-z)}dx=\lambda^2e^{\lambda z}[\frac{e^{-2\lambda x}}{-2\lambda}]_z^{+\infty}=\frac{\lambda}{2}e^{-\lambda z}
$$




## 5. The sum of discrete and continuous r.v.'s

**The sum of discrete and continuous random variables.** Let X be a discrete random variable with PMF pX and let Y be a continuous random variable, independent from X, with PDF fY. Derive a formula for the PDF of the random variable X+Y.



## 6. Using conditional expectation and variance

**Using conditional expectation and variance.** The random variables X and Y are described by a joint PDF which is constant within the unit area quadrilateral with vertices (0,0), (0,1), (1,2), and (1,1). Use the law of total variance to find the variance of X+Y.



## 7. The variance in the stick-breaking problem

**The variance in the stick-breaking problem.** We start with a stick of length ℓ. We break it at a point which is chosen randomly and uniformly over its length, and keep the piece that contains the left end of the stick. We then repeat the same process on the piece that we were left with.

1. What is the expected value of the length of the piece that we are left with after breaking twice?
2. What is the variance of the length of the piece that we are left with after breaking twice?



For a written solution, see Example 4.17 on p. 223 of the text and its continuation on p. 227.



## 8. A coin with random bias

**A coin with random bias.** We toss n times a biased coin whose probability of heads, denoted by q, is the value of a random variable Q with given mean μ and positive variance σ2. Let Xi be a Bernoulli random variable that models the outcome of the ith toss (i.e., Xi=1 if the ith toss is a head). We assume that X1,…,Xn are conditionally independent, given Q=q. Let X be the number of heads obtained in the ntosses.

(a) Use the law of iterated expectations to find E[Xi] and E[X].
(b) Find Cov(Xi,Xj). Are X1,…,Xn independent?
(c) Use the law of total variance to find Var(X). Verify your answer using the covariance result of part (b).



## 9. Widgets and crates

**Widgets and crates.** Widgets are stored in boxes, and then all boxes are assembled in a crate. Let X be the number of widgets in any particular box, and N be the number of boxes in a crate. Assume that X and N are independent integer-valued random variables, with expected value equal to 10, and variance equal to 16. Evaluate the expected value and variance of T, where T is the total number of widgets in a crate.



## 10. Random number of coin flips

**Random number of coin flips.**
(a) You roll a fair six-sided die, and then you flip a fair coin the number of times shown by the die. Assuming that the coin flips are independent, find the expected value and the variance of the number of heads obtained.

(b) Repeat part (a) for the case where you roll two dice, instead of one.





