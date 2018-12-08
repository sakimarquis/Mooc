## 1. Inferring a continuous random variable from a discrete observation

**Inferring a continuous random variable from a discrete observation.** Let Q be a continuous random variable with PDF
$$
f_ Q(q) = \begin{cases} 6q(1-q), &  \mbox{if } 0\leq q\leq 1,\\ 0, &  \mbox{otherwise.}\end{cases}
$$
This Q represents the probability of a success of a Bernoulli random variable X, i.e.,
$$
{\bf P}(X=1\mid Q=q) = q.
$$
Find $f_{Q\mid X}(q\mid x)$ for $x\in \{ 0,1\}$ and all q.



## 2. Inferring a discrete random variable from a continuous observation



**Inferring a discrete random variable from a continuous observation.** Let X be a discrete random variable that takes the values 1 with probability p and −1 with probability 1−p. Let Y be a continuous random variable independent of X with the Laplacian (two-sided exponential) distribution
$$
f_ Y(y) \  = \  \frac{1}{2} \lambda e^{-\lambda |y|},
$$


and let Z=X+Y. Find P(X=1∣Z=z). Check that the expression obtained makes sense for p→0+, p→1−, λ→0+, and λ→∞.



## 3. Inferring the parameter of a uniform: Parts (1)-(4)

**Inferring the parameter of a uniform: Parts (1)-(4).** (*Note:* These parts only involve material covered in Lecture 14.)

## 4. Inferring the parameter of a uniform: Parts (5)-(7)

**Inferring the parameter of a uniform: Parts (5)-(7).** (*Note:* These parts also involve material from Lectures 16 and 17.)

Romeo and Juliet start dating, but Juliet will be late on any date by a random amount X, uniformly distributed over the interval [0,θ]. The parameter θ is unknown and is modeled as the value of a random variable Θ, uniformly distributed between zero and one hour.

1. Assuming that Juliet was late by an amount x on their first date, how should Romeo use this information to update the distribution of Θ?
2. How should Romeo update the distribution of Θ if he observes that Juliet is late by x1,…,xn on the first n dates? Assume that Juliet is late by a random amount X1,…,Xn on the first n dates where, given θ, X1,…,Xn are uniformly distributed between zero and θ and are conditionally independent.
3. Find the MAP estimate of Θ based on the observation X=x.
4. Find the LMS estimate of Θ based on the observation X=x.
5. Calculate the conditional mean squared error for the MAP and the LMS estimates. Compare your results.
6. Derive the linear LMS estimator of Θ based on X.
7. Calculate the conditional mean squared error for the linear LMS estimate. Compare your answer to the results of part (5).



The problem is based on the following examples in the textbook.

1. Example 8.2 on page 414
2. Example 8.2 on page 414
3. Example 8.7 on page 424
4. Example 8.7 on page 424
5. Example 8.12 on pages 432-434
6. Example 8.15 on pages 439-440
7. Example 8.15 on pages 439-440



## 5. Inference example

**Inference example.** Continuous random variables X and Y have a joint PDF given by
$$
f_{X,Y}(x,y) = \left\{  \begin{array}{ll} 2/3, &  \mbox{if $(x,y)$ belongs to the closed shaded region,} \\ 0, &  \mbox{otherwise.} \end{array} \right.
$$
![This figure defines a shaded region in the x-y plane. The positive x and y axes are shown and have markings at x=1, x=2, y=1, and y=2. The shaded region is a symmetric trapezoid whose parallel sides are two diagonal line segments with slope 1, one connecting (D:\Study\Mooc\6.431x\Unit 7 Bayesian inference\Unit 7 Solved problems\images_8_3_lms_2_02.png) and (2,2), and the other connecting (1,0) and (2, 1). The other two sides consist of one horizontal line segment connecting (0,0) and (1,0) and one vertical line segment connecting (2,1) and (2,2). Two dotted lines connect the point (2,2) to its projections on the x and y axes.](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/4122b3ccbbb506c5575f1af65f8460c3/asset-v1:MITx+6.431x+3T2018+type@asset+block/images_8_3_lms_2_02.png)

We want to estimate Y based on X.

1. Find the LMS estimator g(X) of Y.
2. Calculate the conditional mean squared error ${\bf E}\left[\left(Y-g(X)\right)^2\mid X=x\right]$.
3. Calculate the mean squared error ${\bf E}\left[\left(Y-g(X)\right)^2\right]$. Is it the same as E[Var(Y∣X)]?
4. Find L(X), the linear LMS estimator of Y based on X.
5. How do you expect the mean squared error of L(X) to compare to that of g(X)?
6. What problem do you expect to encounter, if any, if you try to find the MAP estimator for Y based on observations of X.

