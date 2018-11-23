## 1. Convergence of the sum of two random variables

**Convergence in probability of the sum of two sequences of random variables.** Show that under the notion of convergence in probability, if Xn→a and Yn→b, then $X_ n+Y_ n\to a+b$. Note that we do not assume independence of $X_n$ and $Y_n$.



## 2. Jensen's inequality

**Jensen's inequality.** A differentiable real-valued function g of a single variable is called **convex** if the first order Taylor approximation of g is an underestimate of the function, that is,
$$
g(c) +(x-c)g'(c) \leq g(x),
$$
for every c and x. Show that if g has this property and if X is a random variable, then
$$
g\big ({\bf E}[X]\big )\leq {\bf E}\big [g(X)\big ].
$$
*Note:* A more general definition of convexity allows the function g to be nondifferentiable. Jensen's inequality is still valid. It is also valid for (suitably defined) convex functions of several variables. That is, if g is convex, then $g\big ({\bf E}[X],{\bf E}[Y]\big )\leq {\bf E}\big [g(X,Y)\big ]$



## 3. Hoeffding's inequality

**Hoeffding's inequality.** The random variables Xi are independent, identically distributed, and each one of them is equally likely to take the values −1 and 1. Let a be positive number. Show that
$$
{\bf P}(X_1+\cdots +X_ n \geq na)\leq e^{-na^2/2}.
$$
*Hint:* Fix some s>0 and use the Markov inequality to get a bound on ${\bf P}\big (\exp \{ s(X_1+\cdots +X_ n)\} \geq e^{sna}\big )$.For any given s, this yields an upper bound on the desired probability. Then, consider the special choice s=a.

**Note:** As long as the Xi are i.i.d., the method used to derive the Hoeffding inequality extends to more general distributions. Under a mild technical assumption, and for any constant a>0, the probability of the event $\{ X_1+\cdots +X_ n \geq n{\bf E}[X_1] +na\}$ falls exponentially with n. The “best" possible bound of this type is known as the *Chernoff bound.*

