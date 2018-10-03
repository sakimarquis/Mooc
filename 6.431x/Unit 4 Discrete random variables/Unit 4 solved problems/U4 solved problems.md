## 1. PMF of a function of a random variable

**PMF of a function of a random variable.** Consider a random variable $X$ such that
$$
p_ X(x) = \left\{ \begin{array}{cl} \frac{x^2}{a},&  \mbox{for } x\in \{ -3,-2,-1,1,2, 3\} ,\\ 0,&  \mbox{otherwise,}\end{array}\right.
$$
where $a>0$ is a real parameter.

1. Find $a$.
2. What is the PMF of the random variable $Z=X^2$?



## 2. Sampling people on buses

**Sampling people on buses.** Four buses carrying 148 job-seeking MIT students arrive at a job convention. The buses carry 40, 33, 25, and 50 students, respectively. One of the students is randomly selected. Let X denote the number of students that were on the bus carrying this randomly selected student. One of the 4 bus drivers is also randomly selected. Let Y denote the number of students on his bus.

1. Which of $E[X]$ or $E[Y]$ do you think is larger? Give your reasoning in words.
2. Compute $E[X]$ and $E[Y]$.



## 3. From tail probabilities to expectations

1. Let X be a random variable that takes nonnegative integer values. Show that
   $$
   {\bf E}[X]=\sum _{k=1}^{\infty }{\bf P}(X\geq k).
   $$
   *Hint*: Express the right-hand side of the above formula as a double summation then interchange the order of the summations.

2. Use the formula in the previous part to find the expectation of a random variable Y whose PMF is defined as follows:
   $$
   p_ Y(y)= \frac{1}{b-a+1}, \qquad y=a,a+1,\ldots ,b
   $$



   where a and b are nonnegative integers with b>a. Note that for y=a,a+1,…,b, pY(y) does not depend explicitly on y since it is a uniform PMF.



## 4. Coupon collector problem

**Coupon collector problem.** A particular professor is known for his arbitrary grading policies. Each paper receives a grade from the set {A,A−,B+,B,B−,C+}, with equal probability, independently of other papers. How many papers do you expect to hand in before you receive each possible grade at least once?



## 5. Conditioning example

**Conditioning example.** Suppose that X and Y are independent, identically distributed, geometric random variables with parameter p. Show that
$$
{\bf P}(X=i \mid X+Y=n)=\frac{1}{n-1}, \qquad \mbox{for $i=1,2,\ldots ,n-1$}.
$$


## 6. Joint PMF drill 1

**Joint PMF drill #1.** Consider a sample space comprised of eight equally likely event points, as shown below:

![img](D:\Study\Mooc\6.431x\Unit 4 Discrete random variables\U4 solved problems\images_2_6_conditioning_1_03_A.png)

1. Which value or values of $x$ **maximize** $E[Y|X=x]$?
2. Which value or values of $y$ **maximize** $Var(X|Y=y)$?
3. Let $R=min(X,Y)$. Provide a clearly labeled sketch of $p_R(r)$,
4. Let A denote the event $X^2≥Y$. Determine numerical values for the quantities $E[XY]$ and $E[XY∣A]$.



## 7. Joint PMF drill 2

**Joint PMF drill #2.** Random variables X and Y can take any value in the set {1,2,3}. We are given the following information about their joint PMF, where the entries indicated by a * are left unspecified:

![A graph with horizontal axis labeled 'x' and the points '1','2','3' marked, and vertical axis labeled 'y' and the points '1','2','3' also marked. A 3 by 3 grid of points are marked and labeled. In the bottow row: the point (D:\Study\Mooc\6.431x\Unit 4 Discrete random variables\U4 solved problems\images_2_7_independence_1_01_A.png) is labeled with '1/12', (2,1) with '2/12', (3,1) with '0'. In the middle row: the point (1,2) is labeled with '2/12', (2,2) with '*', (3,2) with '*'. In the top row: the point (1,3) is labeled with '1/12', (2,3) with '1/12', (3,3) with '*'.](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/ae04e1c79bcb9ccf82991b019a2e4cd0/asset-v1:MITx+6.431x+3T2018+type@asset+block/images_2_7_independence_1_01_A.png)



1) What is pX(1)?
2) Provide a clearly labeled sketch of the conditional PMF of Y given that X=1.
3) What is E[Y∣X=1]?
4) Is there a choice for the unspecified entries that would make X and Y independent?

Let B be the event that X≤2 and Y≤2. We are told that conditioned on B, the random variables X and Y are independent.

5) What is $p_{X,Y}(2,2)$? (If there is not enough information to determine the answer, say so.)
6) What is $p_{X,Y}|B(2,2)$? (If there is not enough information to determine the answer, say so.)



## 8. Joint PMF drill 3

**Joint PMF drill #3.** The joint PMF of the random variables X and Y is given by the following table:

![1538546766256](D:\Study\Mooc\6.431x\Unit 4 Discrete random variables\U4 solved problems\images_2_8.png)

1. Find the value of the constant c.
2. Find $p_Y(2)$.
3. Consider the random variable $Z=YX^2$. Find $E[Z∣Y=2]$.
4. Conditioned on the event that X≠2, are X and Y independent? Give a one-line justification.
5. Find the conditional variance of Y given that X=2.



## 9. Indicator variables: the number of inversions

**Indicator variables: the number of inversions.** There are n persons, numbered 1 to n. Each person i is assigned a seat number $X_i$. The seat numbers are distinct integers in the range $1,…,n$. We assume that the seating is “completely random", that is, the sequence $(X_1,…,X_n)$ is a permutation of the numbers $1,…,n,$ and all permutations are equally likely.

For any i and j, with $1≤i<j≤n$, we say that we have an inversion if $X_i>X_j$. Let N be the number of inversions. Find $E[N]$.



## 10. Indicator variables: the problem of joint lives

**Indicator variables: the problem of joint lives.** Consider 2m persons forming m couples who live together at a given time. Suppose that at some later time, the probability of each person being alive is p, independently of other persons. At that later time, let A be the number of persons that are alive and let S be the number of couples in which both partners are alive. For any number of total surviving persons a, find $E[S∣A=a]​$.