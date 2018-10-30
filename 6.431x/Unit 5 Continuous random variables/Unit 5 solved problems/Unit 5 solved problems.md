## 1. Calculating a CDF

**Calculating a CDF.** Let Z be a continuous random variable with probability density function
$$
f_ z(z)= \left\{  \begin{array}{ll} \gamma (1+z^2), &  \mbox{if $-2<z<1$}, \\ 0, &  \mbox{otherwise}. \end{array} \right.
$$

1. For what value of γ is this possible?
2. Find the cumulative distribution function of Z.



## 2. Mixed distribution example

**Mixed distribution example.** The taxi stand and the bus stop near Al's home are in the same location. Al goes there at a given time and if a taxi is waiting (this happens with probability 2/3) he boards it. Otherwise, he waits for a taxi or a bus to come, whichever comes first. The next taxi will arrive in a time that is uniformly distributed between 0 and 10 minutes, while the next bus will arrive in exactly 5 minutes. Find the CDF and the expected value of Al's waiting time.



## 3. Mean and variance of the exponential

**Mean and variance of the exponential.** Let $λ$ be a positive number. The continuous random variable $X$ is called exponential with parameter $λ$ when its probability density function is
$$
f_{X}(x) = \left\{  \begin{array}{ll} \lambda e^{-\lambda x}, &  \mbox{if $x \geq 0$}, \\ 0, &  \mbox{otherwise}. \end{array} \right.
$$
(a) Find the cumulative distribution function (CDF) of X.
(b) Find the mean of X. 
(c) Find the variance of X. 
(d) Suppose X1, X2, and X3 are independent exponential random variables, each with parameter λ. Find the PDF of Z=max{X1,X2,X3}. 
(e) Find the PDF of W=min{X1,X2}.



## 4. Normal probability calculation

**Normal probability calculation.** Let X and Y be normal random variables, with X∼N(0,1) and Y∼N(1,4).

(a) Find P(X≤1.5) and P(X≤−1) (exactly in terms of Φ, and approximately using the Normal Table.

(b) What is the distribution of Y−12?
(c) Find **P**(−1≤Y≤1) (exactly in terms of Φ, and approximately using the Normal Table.



## 5. Densities and conditioning on an event

**Densities and conditioning on an event.** Let X be a random variable with PDF
$$
f_ X(x)=\begin{cases}  x/4,&  \text {if } 1<x\leq 3,\\ 0,&  \text {otherwise}, \end{cases}
$$
and let A be the event {X≥2}.

(a) Find $E[X], P(A)$, $f_{X∣A}(x)$, and $E[X∣A]$.
(b) Let $Y=X^2$. Find $E[Y]$ and $Var(Y)$.



## 6. Circular uniform PDF

**Circular uniform PDF.** Ben throws a dart at a circular target of radius r. We assume that he always hits the target and that all points of impact (x,y) are equally likely. Compute the joint PDF $f_{X,Y}(x,y)$ of the random variables X and Y, and compute the conditional PDF $f_{X|Y}(x|y)$.

The solution can be found in Example 3.15 on p. 169 of the text.



## 7. The absent minded professor

**The absent minded professor.** An absent-minded professor schedules two student appointments for the same time. The appointment durations are independent and exponentially distributed with mean 30 minutes. The first student arrives on time, but the second student arrives 5 minutes late. What is the expected value of the time between the arrival of the first student and the departure of the second student?



## 8. Uniform probabilities on a triangle

 **Uniform probabilities on a triangle.** Let the random variables X and Y have a joint PDF which is uniform over the triangle with vertices at (0,0), (0,1), and (1,0).

(a) Find the joint PDF of X and Y.
(b) Find the marginal PDF of Y. 
(c) Find the conditional PDF of X given Y. 
(d) Find E[X∣Y=y], and use the total expectation theorem to find E[X] in terms of E[Y].
(e) Use the symmetry of the problem to find the value of E[X].



## 9. Probability that 3 pieces form a triangle

**Probability that 3 pieces form a triangle.** We have a stick of length 1, and we consider breaking it in three pieces as follows. We choose randomly and independently two points on the stick, each point chosen uniformly along the length of the stick, and we break the stick at these two points. What is the probability that the three pieces we are left with can form a triangle?



## 10. Buffon's needle and Monte Carlo simulation

**Buffon's needle and Monte Carlo simulation.** A surface is ruled with parallel lines, which are at distance d from each other. Suppose that we throw a needle of length ℓ on the surface at random. What is the probability that the needle will intersect one of the lines?



## 11. The Bayes rule with continuous random variables

**The Bayes rule with continuous random variables.** Let X and Y be independent continuous random variables with PDFs $f_X$ and $f_Y$, respectively, and let Z=X+Y.

(a) Show that $f_{Z|X}(z∣x)=f_{Y}(z−x)$. *Hint:* Write an expression for the conditional CDF of Z given X, and differentiate.

(b) Assume that X and Y are exponentially distributed with parameter λ. Find the conditional PDF of X, given that Z=z.