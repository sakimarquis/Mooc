## 1. Setting up a Markov chain

**Setting up a Markov chain.** There are n fish in a lake, some of which are green and the rest blue. Each day, Helen catches 1 fish. She is equally likely to catch any one of the n fish in the lake. She throws back all the fish, but paints each green fish blue before throwing it back in. Let Gicorrespond to the situation where there are i green fish left in the lake.

1. Show how to model this fishing exercise as a Markov chain, where {Gi} are the states. Explain why your model satisfies the Markov property.
2. Find the transition probabilities {pij}.
3. List the transient and the recurrent states.



## 2. Markov chain practice I

**Markov chain practice I.** Consider the following Markov chain, with states labelled S0,S1,…,S5:

![img](D:\Study\Mooc\6.431x\Unit 10 Markov chains\Unit 10 Solved problems\images_7_1_markov_discrete_1_04_A.png)Given that the above process is in state S0 just before the first trial, determine by inspection the probability that:

(a) The process enters S2 for the first time as the result of the kth trial.
(b) The process never enters S4.
(c) The process enters S2 and then leaves S2 on the next trial.
(d) The process enters S1 for the first time on the third trial.
(e) The process is in state S3 immediately after the nth trial.



## 3. Markov chain practice II

**Markov chain practice II.** The Markov chain shown below is in state 3 immediately before the first trial.

![img](D:\Study\Mooc\6.431x\Unit 10 Markov chains\Unit 10 Solved problems\images_7_2_markov_classification_1_03_A.png)

(a) Indicate which states, if any, are recurrent, transient, and periodic.
(b) Find the probability that the process is in state 3 after n trials.
(c) Find the expected number of trials up to and including the trial on which the process leaves state 3.
(d) Find the probability that the process never enters state 1.
(e) Find the probability that the process is in state 4 after 10 trials.
(f) Given that the process is in state 4 after 10 trials, find the probability that the process was in state 4 after the first trial.



## 4. Markov chain practice III

 Bookmark this page

**Markov chain practice III.** Consider the following Markov chain:

![img](D:\Study\Mooc\6.431x\Unit 10 Markov chains\Unit 10 Solved problems\images_7_3_markov_steady_1_11_A.png)

The steady-state probabilities for this process are:
$$
\pi _1 = \frac{6}{31},\quad \pi _2=\frac{9}{31},\quad \pi _3 = \frac{6}{31},\quad \pi _4=\frac{10}{31}.
$$
Assume the process is in state 1 just before the first transition.

1. Determine the expected value and variance of K, the number of transitions up to and including the next transition on which the process returns to state 1.
2. What is the probability that the state of the system resulting from transition 1000 is neither the same as the state resulting from transition 999 nor the same as the state resulting from transition 1001?



## 5. Mean first-passage and recurrence times

**Mean first-passage and recurrence times.** On any given week while taking 6.431x, a student can be either up-to-date on learning the material, or she may have fallen behind. If she is up-to-date in a given week, the probability that she will be up-to-date (or behind) in the next week is 0.8 (or 0.2, respectively). If she is behind in the given week, the probability that she will be up-to-date (or behind) in the next week is 0.6 (or 0.4, respectively). We assume that these probabilities do not depend on whether she was up-to-date or behind in previous weeks, so we can model the situation as a 2-state Markov chain where state 1 is the case when the student is up-to-date and state 2 is the case when the student is behind.

1. Calculate the mean first passage time to state 1, starting from state 2.
2. Calculate the mean recurrence time to state 1.