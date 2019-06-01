## 分布收敛(convergence in distribution):

**定义：**
![X_n](https://www.zhihu.com/equation?tex=X_n)依分布收敛至X，记作![X_n \overset{d}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7Bd%7D%7B%5Crightarrow%7DX)，意味着：![F_n(x)\rightarrow F(x)](https://www.zhihu.com/equation?tex=F_n%28x%29%5Crightarrow+F%28x%29)，对于所有F的连续点x。

也就是说，当n很大的时候，![X_n](https://www.zhihu.com/equation?tex=X_n)的**累积函数**和X的**累积函数差不多**。

直观上而言，依分布收敛只在乎随机变量的**分布**，而不在乎他们之间的**相互关系**。

举例而言，倘若已知![X_n \overset{d}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7Bd%7D%7B%5Crightarrow%7DX)，假设![Y=-X](https://www.zhihu.com/equation?tex=Y%3D-X)。对于任意一个发生的事件，Y与X的取值正好差了一个负号。但这并不影响X与Y有相同的累积函数，即![F_X(z)=F_Y(z)](https://www.zhihu.com/equation?tex=F_X%28z%29%3DF_Y%28z%29)。如此一来，![X_n \overset{d}{\rightarrow}Y](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7Bd%7D%7B%5Crightarrow%7DY)。更一般的情况而言，只要X与Y有相同的累计函数，即same distributed，即使![P(X=Y)<1](https://www.zhihu.com/equation?tex=P%28X%3DY%29%3C1)，也有![X_n \overset{d}{\rightarrow}Y](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7Bd%7D%7B%5Crightarrow%7DY)。因为依分布收敛仅仅在乎分布，而不在乎相互之间的关系。



## 概率收敛(convergence in probability):

**定义：**
![X_n](https://www.zhihu.com/equation?tex=X_n)依概率收敛至X，记作![X_n \overset{P}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7BP%7D%7B%5Crightarrow%7DX)，意味着：![P(|X_n-X|\leq \varepsilon )\rightarrow 1](https://www.zhihu.com/equation?tex=P%28%7CX_n-X%7C%5Cleq+%5Cvarepsilon+%29%5Crightarrow+1)，当![n\rightarrow \infty](https://www.zhihu.com/equation?tex=n%5Crightarrow+%5Cinfty)，![\forall \varepsilon >0](https://www.zhihu.com/equation?tex=%5Cforall+%5Cvarepsilon+%3E0)。

也就是说，当n很大的时候，对任意发生的事件，![X_n](https://www.zhihu.com/equation?tex=X_n)的**值**和X的**值差不多**，即![|(X_n-X)(\omega )|](https://www.zhihu.com/equation?tex=%7C%28X_n-X%29%28%5Comega+%29%7C)很小。

直观上而言，依概率收敛在乎的是**随机变量的值**。

这样说来，前面依分布收敛的例子如果套在概率收敛上就会出现问题。如果![X_n \overset{P}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7BP%7D%7B%5Crightarrow%7DX)，但对于任何一个与X分布一样的Y，但![P(X=Y)<1](https://www.zhihu.com/equation?tex=P%28X%3DY%29%3C1)，![X_n \overset{P}{\rightarrow}Y](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7BP%7D%7B%5Crightarrow%7DY)一定不成立，因为X与Y只是分布相同，而值不同。但反而言之，如果![X_n \overset{P}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7BP%7D%7B%5Crightarrow%7DX)，即它们的值都差不多了，那么它们的分布一定也差不多，即![X_n \overset{d}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7Bd%7D%7B%5Crightarrow%7DX)。因此，依概率收敛比依分布收敛要强，即![X_n \overset{P}{\rightarrow}X\Rightarrow X_n \overset{d}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7BP%7D%7B%5Crightarrow%7DX%5CRightarrow+X_n+%5Coverset%7Bd%7D%7B%5Crightarrow%7DX)。

但在某种情况下，取值就可以确定分布。即X取某个常数的情况下。此时X的取值和X的分布唯一确定。即此时会有依分布收敛和依概率收敛等价，即![X_n \overset{d}{\rightarrow}c\Leftrightarrow X_n \overset{P}{\rightarrow}c](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7Bd%7D%7B%5Crightarrow%7Dc%5CLeftrightarrow+X_n+%5Coverset%7BP%7D%7B%5Crightarrow%7Dc)。



## Lp收敛(convergence in Lp):

**定义：**
![X_n](https://www.zhihu.com/equation?tex=X_n)依Lp收敛至X，记作![X_n \overset{L_p}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7BL_p%7D%7B%5Crightarrow%7DX)，意味着：![E(X_n-X)^p\rightarrow 0](https://www.zhihu.com/equation?tex=E%28X_n-X%29%5Ep%5Crightarrow+0)，当![n\rightarrow \infty](https://www.zhihu.com/equation?tex=n%5Crightarrow+%5Cinfty)，![p\geq 1](https://www.zhihu.com/equation?tex=p%5Cgeq+1)。
在p＝2时即为均方收敛。

直观上而言，均方收敛在乎的也是**随机变量的值**，但其要求比依概率收敛更加严格。

之所以更加严格，是因为概率测度可以被均方测度所限制，其思想可以近似由Chebyshev不等式看到。![P(|X-\mu|\geq \varepsilon )\leq \frac{E(X-\mu)^2}{\varepsilon ^2}](https://www.zhihu.com/equation?tex=P%28%7CX-%5Cmu%7C%5Cgeq+%5Cvarepsilon+%29%5Cleq+%5Cfrac%7BE%28X-%5Cmu%29%5E2%7D%7B%5Cvarepsilon+%5E2%7D)。因此![X_n \overset{L^2}{\rightarrow}X\Rightarrow X_n \overset{P}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7BL%5E2%7D%7B%5Crightarrow%7DX%5CRightarrow+X_n+%5Coverset%7BP%7D%7B%5Crightarrow%7DX).

- **几乎处处收敛(convergence almost surely):**

**定义：**
![X_n](https://www.zhihu.com/equation?tex=X_n)几乎处处收敛至X，记作![X_n \overset{a.s.}{\rightarrow}X](https://www.zhihu.com/equation?tex=X_n+%5Coverset%7Ba.s.%7D%7B%5Crightarrow%7DX)，意味着：![P(X_n\rightarrow X) = 1](https://www.zhihu.com/equation?tex=P%28X_n%5Crightarrow+X%29+%3D+1)，当![n\rightarrow \infty](https://www.zhihu.com/equation?tex=n%5Crightarrow+%5Cinfty)。

直观上而言，几乎处处收敛在乎的也是**随机变量的值**，但其要求也比依概率收敛更加严格。

如果没有接触过实变函数的知识，几乎处处收敛对于连续型随机变量可能比较难以理解。我们这边用离散型随机变量进行直观解释，以避免0测度下的一些问题。

对于![X_n\sim Ber(p_n)](https://www.zhihu.com/equation?tex=X_n%5Csim+Ber%28p_n%29)，即以概率![p_n](https://www.zhihu.com/equation?tex=p_n)取1，其余为0的随机变量。其依概率收敛到1意味着，![X_n](https://www.zhihu.com/equation?tex=X_n)和1的值都**差不多**，而且**随着n越来越大，不相等的概率越来越小**。转而言之，**出现0的概率越来越小，极限为0**。但几乎处处收敛至1要求，存在N，![n>N](https://www.zhihu.com/equation?tex=n%3EN)时，![X_n=1](https://www.zhihu.com/equation?tex=X_n%3D1)，即![X_n](https://www.zhihu.com/equation?tex=X_n)和1的值都**在n很大时必须相等**，即![X_n](https://www.zhihu.com/equation?tex=X_n)取0的概率在某个N后必须为0。前者限制其尾部概率收敛至0，但后者限制尾部概率为0。

**结论：**
**(1)几乎处处收敛和Lp收敛最强，依概率收敛其次，依分布收敛最弱。**
**(2)几乎处处收敛和Lp收敛并无推导关系。**
**(3)在收敛到常数时，依概率收敛和依分布收敛等价。**

