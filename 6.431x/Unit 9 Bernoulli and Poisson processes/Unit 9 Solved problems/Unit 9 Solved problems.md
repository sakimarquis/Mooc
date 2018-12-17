## 1. Bernoulli process practice I

**Bernoulli process practice I.** You are visiting the rainforest, but unfortunately your insect repellent has run out. As a result, at each second, a mosquito lands on your neck with probability 0.5, independently of what happens at any other second. If one lands, with probability 0.2 it bites you and with probability 0.8 it never bothers you, independently of other mosquitoes.

1) What is the expected time between successive mosquito bites?
2) What is the variance of the time between successive mosquito bites?

In addition, at each second, a tick lands on your neck with probability 0.1, independently of what happens at any other second. If one lands, with probability 0.7 it bites you and with probability 0.3 it never bothers you, independently of other ticks and mosquitoes.

3) Now, what is expected time between successive bug (either mosquito or tick) bites?
4) What is the variance of the time between successive bug bites?



## 2. Bernoulli process practice II

**Bernoulli process practice II.** A computer system carries out tasks submitted by two users. Time is divided into slots. A slot can be idle, with probability pI=1/6, and busy with probability pB=5/6. During a busy slot, there is probability p1∣B=2/5 (respectively, p2∣B=3/5) that a task from user 1 (respectively, 2) is executed. We assume that events related to different slots are independent.

(a) Find the probability that a task from user 1 is executed for the first time during the 4th slot.
(b) Given that exactly 5 out of the first 10 slots were idle, find the probability that the 6th idle slot is slot 12.
(c) Find the expected number of slots up to and including the 5th task from user 1.
(d) Find the expected number of busy slots up to and including the 5th task from user 1.
(e) Find the PMF, mean, and variance of the number of tasks from user 2 until the time of the 5th task from user 1.



## 3. Poisson process drill

**Poisson process drill.** A train bridge is constructed across a wide river. Trains arrive at the bridge according to a Poisson process of rate λ=3per day.

1. If a train arrives on day 0, find the probability that there will be no trains on days 1, 2, and 3.
2. Find the probability that the next train to arrive after the first train on day 0, takes more than 3 days to arrive.
3. Find the probability that no trains arrive in the first 2 days, but 4 trains arrive on the 4th day.
4. Find the probability that it takes more than 2 days for the 5th train to arrive at the bridge.



## 4. Poisson process practice I

**Poisson process practice I.** Beginning at time t=0, we start using bulbs, one at a time, to illuminate a room. Bulbs are replaced immediately upon failure. Each new bulb is selected independently by an equally likely choice between a type-A bulb and a type-B bulb. The lifetime, X, of any particular bulb of a particular type is a random variable, independent of everything else, with the following PDF:

for type-A Bulbs: $\displaystyle f_ X(x) = \begin{cases}  e^{-x}, &  \mbox{if } x \geq 0,\\ 0 ,&  \mbox{otherwise;}\end{cases}\qquad$ 

for type-B Bulbs: $\displaystyle f_ X(x) = \begin{cases}  3 e^{-3x}, &  \mbox{if } x \geq 0,\\ 0, &  \mbox{otherwise.}\end{cases}$



## 5. Poisson process practice II

**Poisson process practice II.** A service station handles jobs of two types, A and B. (Multiple jobs can be processed simultaneously.) Arrivals of the two job types are independent Poisson processes with parameters λA=3 and λB=4 per minute, respectively. Type A jobs stay in the service station for exactly one minute. Each type B job stays in the service station for a random but integer amount of time which is geometrically distributed, with mean equal to 2, and independent of everything else. The service station started operating at some time in the remote past.

1. What is the mean, variance, and PMF of the total number of jobs that arrive within a given three-minute interval?
2. We are told that during a 10-minute interval, exactly 10 new jobs arrived. What is the probability that exactly 3 of them are of type A?
3. At time 0, no job is present in the service station. What is the PMF of the number of type B jobs that arrive in the future, but before the first type A arrival?



## 6. Competing exponentials

**Competing exponentials.** Let X, Y, and Z be independent exponential random variables with parameters λ, μ, and ν, respectively. Find P(X<Y<Z).



## 7. Random incidence under Erlang arrivals

**Random incidence under Erlang arrivals.** Consider an arrival process in which the interarrival times are independent Erlang random variables or order 2, with mean 2/λ. Assume that the arrival process has been ongoing for a very long time. An external observer arrives at a given time t. Find the PDF of the length of the interarrival interval that contains t.