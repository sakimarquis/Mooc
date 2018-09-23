## 1. Two five-sided dice

### Problem 1. Two five-sided dice

You roll two five-sided dice. The sides of each die are numbered from 1 to 5. The dice are “fair"" (all sides are equally likely), and the two die rolls are independent.

Part (a): Event A is “the total is 10" (i.e., the sum of the results of the two die rolls is 10).

1. Is event A independent of the event “at least one of the dice resulted in a 5""?

   No

2. Is event A independent of the event “at least one of the dice resulted in a 1""?

   No

Part (b): Event B is “the total is 8."

1. Is event B independent of getting “doubles"" (i.e., both dice resulting in the same number)?

    No

2. Given that the total was 8, what is the probability that at least one of the dice resulted in a 3?

   2/3



## 2. A reliability problem

### Problem 2. A reliability problem

Consider the communication network shown in the figure below and suppose that each link can fail with probability p. Assume that failures of different links are independent.

![There is a point A, and two line segments originate from point A to the right. The top line segment is labeled Link 1 and the bottom line segment is labeled Link 3. Link 1 is then connected on its right to another line segment labeled Link 2, and Link 3 is connected on its right to another line segment labeled Link 4. Link 2 and Link 4 are joined on their right ends to a single point, so that Links 1,2,3 and 4 together make a diamond-shape. From the single point at the ends of Links 2 and 4 is another line segment labeled Link 5, and its right end is labeled B. ](D:\Study\Mooc\6.431x\Unit 2 Conditioning and independence\images_2_02new.jpg)

1. Assume that p=1/3. Find the probability that there exists a path from A to B along which no link has failed. (Give a numerical answer.)

   112/243

2. Given that exactly one link in the network has failed, find the probability that there exists a path from A to B along which no link has failed. (Give a numerical answer.)

   4/5



## 3. Oscar's lost dog in the forest

### Problem 3. Oscar's lost dog in the forest

Oscar has lost his dog in either forest A (with probability 0.4) or in forest B (with probability 0.6).

If the dog is in forest A and Oscar spends a day searching for it in forest A, the conditional probability that he will find the dog that day is 0.25. Similarly, if the dog is in forest B and Oscar spends a day looking for it there, he will find the dog that day with probability 0.15.

The dog cannot go from one forest to the other. Oscar can search only in the daytime, and he can travel from one forest to the other only overnight.

The dog is alive during day 0, when Oscar loses it, and during day 1, when Oscar starts searching. It is alive during day 2 with probability 2/3. In general, for n≥1, if the dog is alive during day n−1, then the probability it is alive during day n is 2/(n+1). The dog can only die overnight. Oscar stops searching as soon as he finds his dog, either alive or dead.

a) In which forest should Oscar look on the first day of the search to maximize the probability he finds his dog that day?

P(A) = 0.4 * 0.25 = 0.1

P(B) = 0.6 * 0.15 = 0.09

Forest A



b) Oscar looked in forest A on the first day but didn't find his dog. What is the probability that the dog is in forest A?

0.3/(0.3 + 0.6)



c) Oscar flips a fair coin to determine where to look on the first day and finds the dog on the first day. What is the probability that he looked in forest A?

0.5 * 0.1/(0.5 * 0.1 + 0.5 * 0.09)



d) Oscar decides to look in forest A for the first two days. What is the probability that he finds his dog alive for the first time on the second day?

P(found alive) = 2/3 * 0.4 * 0.25 * 0.75 = 0.05



e) Oscar decides to look in forest A for the first two days. Given that he did not find his dog on the first day, find the probability that he does not find his dog dead on the second day.

P(found dead) = 1/3 * 0.4 * 0.25 * 0.75 = 0.025

P(not found) = 0.4 * 0.75 + 0.6 * 0.85 = 0.81

P(found) = P(found dead) + P(found alive)

P(found dead|P(not found)∩P(found)) = P(found dead)∩P(not found)∩P(found) / P(not found)∩P(found)



f) Oscar finally finds his dog on the fourth day of the search. He looked in forest A for the first 3 days and in forest B on the fourth day. Given this information, what is the probability that he found his dog alive?

2/3 * 2/4 * 2/5





## 4. Serap and her umbrella

### Problem 4. Serap and her umbrella

Before leaving for work, Serap checks the weather report in order to decide whether to carry an umbrella. On any given day, with probability 0.2the forecast is “rain"" and with probability 0.8 the forecast is “no rain"". If the forecast is “rain"", the probability of actually having rain on that day is 0.8. On the other hand, if the forecast is “no rain"", the probability of actually raining is 0.1.

1. One day, Serap missed the forecast and it rained. What is the probability that the forecast was “rain""?

   2/3

2. Serap misses the morning forecast with probability 0.2 on any day in the year. If she misses the forecast, Serap will flip a fair coin to decide whether to carry an umbrella. (We assume that the result of the coin flip is independent from the forecast and the weather.) On any day she sees the forecast, if it says “rain"" she will always carry an umbrella, and if it says “no rain"" she will not carry an umbrella. Let U be the event that “Serap is carrying an umbrella"", and let N be the event that the forecast is “no rain"". Are events U and Nindependent?

    No

3. Serap is carrying an umbrella and it is not raining. What is the probability that she saw the forecast?

   P(saw forecast rain and rain) = 0.032

   P(flip to take and forecast rain and rain) = 0.2 * 0.38

   0.032/(0.032 + (0.2 * 0.38) = 0.2963



