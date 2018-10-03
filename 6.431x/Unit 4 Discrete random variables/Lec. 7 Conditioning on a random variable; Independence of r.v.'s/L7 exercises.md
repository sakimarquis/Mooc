## 3. Exercise: Conditional PMFs

For each of the formulas below, state whether it is true or false.

a)  $p_{X,Y,Z}(x,y,z)=p_ Y(y)\,  p_{Z\mid Y}(z\mid y) \,  p_{X\mid Y,Z}(x\mid y,z)$

b) $p_{X,Y\mid Z}(x,y\mid z) =p_ X(x)\, p_{Y\mid Z}(y\mid z)$

c) $p_{X,Y\mid Z}(x,y\mid z)=p_{X\mid Z}(x\mid z)\, p_{Y\mid X,Z}(y\mid x,z)$

d) $\displaystyle {\sum _ x p_{X,Y\mid Z}(x,y\mid z)=1}$

e) $\displaystyle {\sum _ x\sum _ y p_{X,Y\mid Z}(x,y\mid z)=1}$

f) $\displaystyle {p_{X,Y\mid Z}(x,y\mid z)=\frac{p_{X,Y,Z}(x,y,z)}{p_ Z(z)}}$

g) $\displaystyle {p_{X\mid Y,Z}(x\mid y, z)=\frac{p_{X,Y,Z}(x,y,z)}{p_{Y,Z}(y,z)}}$



#### Solotion

a) True. This is the usual multiplication rule for the probability of three events occurring simultaneously.

b) False. This does not follow from any of the formulas we have developed.

c) True. This is the usual multiplication rule for the event ${X=x and Y=y}$, in a conditional model in which it is given that the event ${Z=z}$ has occurred.

d) False. The left-hand side is a function of y, whereas the right-hand side is not.

e) True. This is the usual normalization property, in a conditional model in which it is given that the event ${Z=z}$ has occurred.

f) True. This is just the formula for the conditional probability $P(X=x,Y=y∣Z=z)$.

g) True. This is just the formula for the conditional probability $P(X=x∣Y=y,Z=z)$.



## 5. Exercise: The expected value rule with conditioning

For each of the formulas below, state whether it is true or false.

1. $\displaystyle {{\bf E}[g(X,Y)\mid Y=2]=\sum _ x g(x,y) p_{X,Y}(x,y)}$
2. $\displaystyle {{\bf E}[g(X,Y)\mid Y=2]=\sum _ x g(x,y) p_{X,Y}(x,2)}$
3. $\displaystyle {{\bf E}[g(X,Y)\mid Y=2]=\sum _ x g(x,2) p_{X,Y}(x,2)}$
4. $\displaystyle {{\bf E}[g(X,Y)\mid Y=2]=\sum _ x g(x,2) p_{X\mid Y}(x\mid 2)}$
5. $\displaystyle {{\bf E}[g(X,Y)\mid Y=2]=\sum _ x g(x,2) \frac{p_{X,Y}(x,2)}{p_ Y(2)}}$
6. $\displaystyle {{\bf E}[g(X,Y)\mid Y=2]=\sum _ x \sum _ y g(x,y) p_{X,Y\mid Y}(x,y\mid 2)}$



#### Solution

1-3) There is no reason for any of the first three formulas to be true.

4) True. This is just the usual expected value rule, in a model in which the event ${Y=2}$ is known to have occurred. Given the information that $Y=2$, the function $g(x,y)$ is replaced by $g(x,2)$, and we are dealing with a function $g(x,2)$ of a single variable $x$. We apply the expected value rule for a function of a single variable, but since we are within a conditional model, we need to use the conditional PMF of $X$.

5) True. This is the same as the fourth statement, except that we have substituted in the definition of $p_{X\mid Y}(x\mid 2)$.

6) True. This is just the expected value rule for a function of two variables, applied within a conditional universe where the event ${Y=2}$ is known to have occurred.

Notice that $p_{X,Y\mid Y}(x,y\mid 2)$ will be zero for any $y≠2$. And for $y=2$,
$$
p_{X,Y\mid Y}(x,2\mid 2)={\bf P}(X=x, Y=2\mid Y=2)={\bf P}(X=x\mid Y=2)=p_{X\mid Y}(x\mid 2),
$$
so that the sixth formula agrees with the fourth one.



