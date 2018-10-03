## 4. Proving binomial identities via counting

Binomial identities (i.e., identities involving binomial coefficients) can often be proved via a counting interpretation. For each of the binomial identities given below, select the counting problem that can be used to prove it.


$$
\displaystyle n\binom {2n}{n}= \displaystyle 2n\binom {2n-1}{n-1}
$$
Out of 2n people, we want to choose a committee of n people, one of whom will be its chair. In how many different ways can this be done? 
$$
\displaystyle \binom {2n}{n} = \displaystyle \sum _{i=0}^ n \binom {n}{i}^2 =\displaystyle \sum _{i=0}^ n \binom {n}{i}\binom {n}{n-i}
$$
In a group of 2n people, consisting of n boys and n girls, we want to select a committee of n people. In how many ways can this be done? 


$$
\displaystyle 2^{2n} =\displaystyle \sum _{i=0}^{2n} \binom {2n}{i}
$$
How many subsets does a set with 2n elements have? 


$$
\displaystyle n2^{n-1} = \displaystyle \sum _{i=0}^ n \binom {n}{i}i
$$
Out of n people, we want to form a committee consisting of a chair and other members. We allow the committee size to be any integer in the range 1,2,…,n. How many choices do we have in selecting a committee-chair combination? 



# 5.Hats in a box

Each one of n persons, indexed by 1,2,…,n, has a clean hat and throws it into a box. The persons then pick hats from the box, at random. Every assignment of the hats to the persons is equally likely. In an equivalent model, each person picks a hat, one at a time, in the order of their index, with each one of the remaining hats being equally likely to be picked. Find the probability of the following events.

(You need to answer all 5 questions before you can submit.)

1. Every person gets his or her own hat back.

$$
\displaystyle{\frac{1}{n!}}\\[15pt]
$$

2. Each one of persons 1,…,m gets his or her own hat back, where 1≤m≤n.
   $$
   \displaystyle{\frac{(n-m)!}{n!}}\\[15pt]
   $$


3. Each one of persons 1,…,m gets back a hat belonging to one of the last m persons (persons n−m+1,…,n), where 1≤m≤n.

$$
\displaystyle{\frac{\displaystyle{1}}{\displaystyle{n \choose m}}}\\[15pt]
$$

4. Persons 1,…,m will pick up clean hats.

$$
\displaystyle{{(1-p)}^{n-m}}\\[15pt]
$$

5. Exactly m persons will pick up clean hats.

$$
\displaystyle{{n \choose m}(1-p)^mp^{n-m}}\\[15pt]
$$

