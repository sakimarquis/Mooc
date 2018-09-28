## 11. Exercise: The binomial PMF

You roll a fair six-sided die (all 6 of the possible results of a die roll are equally likely) 5 times, independently. Let X be the number of times that the roll results in 2 or 3. Find the numerical values of the following.

**Solution:**

a) A value of 2.5 is not possible for X since the number of rolls must be an integer, and therefore pX(2.5)=0.

b) For each die roll, there is a probability 2/6=1/3 of obtaining a 2 or a 3. Hence, the random variable X is binomial with parameters n=5 and p=1/3, so that p_ X(1)={5 \choose 1} \cdot (1/3)\cdot (2/3)^4\approx 0.32922 ≈ 0.32922.



## 19. Exercise: The expected value rule

Let X be a uniform random variable on the range {−1,0,1,2}. Let Y=X4. Use the expected value rule to calculate E[Y].

We are dealing with Y=g(X), where g is the function defined by $g(x)=x^4$. Thus,
$$
{\bf E}[Y]={\bf E}[X^4]=\sum _ x x^4 p_ X(x) =(-1)^4\cdot \frac{1}{4} + 0^4\cdot \frac{1}{4} + 1^4\cdot \frac{1}{4} +2^4\cdot \frac{1}{4}= \frac{1}{4}+\frac{1}{4}+\frac{16}{4}=4.5.
$$




## 21. Exercise: Linearity of expectations

The random variable X is known to satisfy E[X]=2 and E[X2]=7. Find the expected value of 8−X and of (X−3)(X+3).



**Solution:**

a) The random variable 8−X is of the form aX+b, with a=−1 and b=8. By linearity, E[8−X]=−E[X]+8=−2+8=6.

b) The random variable (X−3)(X+3) is equal to $X^2−9$ and therefore its expected value is $E[X^2]−9=7−9$=−2.