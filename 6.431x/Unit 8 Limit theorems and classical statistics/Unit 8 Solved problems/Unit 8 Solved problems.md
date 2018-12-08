## 1. Convergence in probability example

**Convergence in probability example.** The random variable X is uniformly distributed between −1 and 1. Let X1, X2,… be independent identically distributed random variables with the same distribution as X. Determine which, if any, of the following sequences Xi converge in probability, and if so, determine the limits.

1. $X_i$
2. ${\displaystyle Y_ i = \frac{X_ i}{i}}$
3. $Z_ i = (X_ i)^ i$



## 2. Convergence in probability and in the mean square - Part I

**Convergence in probability and in the mean square - Part I.** Let Xn and Yn have the distributions shown below.

![This figure consists of two panels showing two probability mass functions on the x-y plane; the left panel for the variable x and the right panel for the variable y. Only the positive x and y axes are shown for both panels. In the left panel, the x axis is labelled 'x' and the y axis is labelled 'p_x_n (D:\Study\Mooc\6.431x\Unit 8 Limit theorems and classical statistics\Unit 8 Solved problems\images_5_3_convergence_1_02_A.png)'. The PMF in the left panel consists of two masses, one at x=0 with a height of 1-(1/n), and one at x=1 with a height of 1/n. In the right panel, the x axis is labelled 'y' and the y axis is labelled 'p_y_n (y)'. The PMF in the right panel consists of two masses, one at y=0 with a height of 1-(1/n) and one at y=n with a mass of 1/n.](https://prod-edxapp.edx-cdn.org/assets/courseware/v1/815635845a5b134fa78b967fe4784598/asset-v1:MITx+6.431x+3T2018+type@asset+block/images_5_3_convergence_1_02_A.png)



(a) Find the expected value and variance of $X_n$ and $Y_n$.

(b) What (if anything) does the Chebyshev inequality tell us about the convergence of  $X_n$ and $Y_n$?

(c) Is  $Y_n$ convergent in probability? If so, to what value?

(d) If a sequence of random variables converges in probability to a, does the corresponding sequence of expected values converge to a? Prove or give a counterexample.



## 3. Convergence in probability and in the mean square - Part II

**Convergence in probability and in the mean square - Part II.** A sequence of random variables is said to converge to a number c in the **mean square**, if
$$
\displaystyle \lim _{n\to \infty } {\bf E}\left[(X_ n-c)^2\right]=0.
$$
(e) Use Markov's inequality to show that convergence in the mean square implies convergence in probability.

(f) Give an example that shows that convergence in probability does not imply convergence in the mean square.



## 4. Probability bounds

**Probability bounds.** Let X1,…,X10 be independent random variables, uniformly distributed over the unit interval [0,1].

1. Find an upper bound on ${\bf P}(X_1+\cdots +X_{10} \geq 7)$ using the Markov inequality.
2. Find an upper bound on ${\bf P}(X_1+\cdots +X_{10} \geq 7)$ using the Chebyshev inequality.
3. Estimate ${\bf P}(X_1+\cdots +X_{10} \geq 7)$ using the central limit theorem.



## 5. Using the CLT to estimate the probability of a wrong decision

**Using the CLT to estimate the probability of a wrong decision.** Before starting to play the roulette in a casino, you want to look for biases that you can exploit. You therefore watch 100 rounds that result in a number between 1 and 36, and count the number of rounds for which the result is odd. If the count exceeds 55, you decide that the roulette is not fair. Assuming that the roulette is fair, find an approximation for the probability that that you will make the wrong decision.



## 6. Using the CLT

**Using the CLT.** A factory produces Xn gadgets on day n, where the Xn are independent and identically distributed random variables, with mean 5 and variance 9.

1. Find an approximation to the probability that the total number of gadgets produced in 100 days is less than 440.
2. Find (approximately) the largest value of n such that ${\bf P}\left(X_1+\cdots +X_ n \geq 200 + 5n\right)\leq 0.05.$
3. Let N be the first day on which the total number of gadgets produced exceeds 1000. Calculate an approximation to the probability that N≥220.



## 7. An unbiased variance estimator

**An unbiased variance estimator.** Let $X_1,X_2,\ldots ,X_ n$ be independent identically distributed random variables with a common mean θ and a common variance v. Let $M_ n=(X_1+\cdots +X_ n)/n$, which is the sample mean, and consider the following estimator of the variance:
$$
\hat S_ n^2=\frac{1}{n-1}\sum _{i=1}^ n (X_ i-M_ n)^2.
$$
Show that this estimator is unbiased, that is,
$$
{\bf E}\big [\hat S_ n^2\big ]=v.
$$



A written solution to this problem can be found on pages 467-468 of the text.

![1543038178349](D:\Study\Mooc\6.431x\Unit 8 Limit theorems and classical statistics\Unit 8 Solved problems\unbiased variance estimator.png)