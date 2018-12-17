## 1. Poisson versus normal approximation to the binomial

**Poisson versus normal approximation to the binomial.** We have seen that a binomial random variable with parameters n and p can be approximated by a normal random variable (central limit theorem) but also by a Poisson random variable. Are these two facts contradictory? Fortunately not; the two approximations apply to different regimes:

1. If we fix p and let n→∞, we are in the setting where the central limit theorem applies.
2. If we let n→∞, p→0, while keeping the product np fixed, the Poisson approximation applies.

Finally, we explain why a Poisson random variable with a large mean is approximately normal (another application of the central limit theorem). For this reason, there is a regime (p very small, but np very large) in which the two approximations agree.



## 2. Poisson arrivals during an exponential interval

**The number of Poisson arrivals during an interval of exponential length.** Let $N_t$ denote the number of arrivals of a Poisson process with parameter λ within an interval of length t. Let also T be an interval with length that is exponentially distributed with parameter μ and is independent of the Poisson process. Show that $N_T$+1 is geometrically distributed with parameter μ/(λ+μ).



## 3. Sums of a binomial and a Poisson-distributed number of Bernoulli r.v.'s

**Sums of a binomial and a Poisson-distributed number of Bernoulli r.v.'s.** Let X1,X2,… be independent Bernoulli random variables with parameter p, and N be a random variable that takes integer values and is independent of Xi, i=1,2,…. Let Y=X1+⋯+XN for positive values of N, and let Y=0 when N=0.

1. If N is binomial with parameters m and q, then Y is binomial with parameters m and pq.
2. If N is Poisson with parameter λ, then Y is Poisson with parameter λp.



## 4. Sum of a geometrically-distributed number of geometric and exponential r.v.'s

**Sum of a geometrically-distributed number of geometric and exponential r.v.'s.** Let N be a geometric random variable with parameter q, and let X1,X2,… be random variables that are independent and independent of N. Let Y=X1+⋯+XN.

1. If Xi is geometric with parameter p, then Y is geometric with parameter pq.
2. If Xi is exponential with parameter λ, then Y is exponential with parameter λq.