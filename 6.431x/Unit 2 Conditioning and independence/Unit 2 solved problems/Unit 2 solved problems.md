# 1 Conditional probability example

**Conditional probability example.** We roll two fair 6-sided dice. Each one of the 36 possible outcomes is assumed to be equally likely.

(a) Find the probability that doubles are rolled (i.e., both dice have the same number).

(b) Given that the roll results in a sum of 4 or less, find the conditional probability that doubles are rolled.

(c) Find the probability that at least one die roll is a 6.

(d) Given that the two dice land on different numbers, find the conditional probability that at least one die roll is a 6.



Solution:


![img](D:\Study\Mooc\6.431x\Unit 2 Conditioning and independence\Solved problems\recitation_conditional_probability_example_sol.jpg)




# 2 A chess tournament problem

**A chess tournament problem.** This year's Belmont chess champion is to be selected by the following procedure. Bo and Ci, the leading challengers, first play a two-game match. If one of them wins both games, he gets to play a two-game **second round** with Al, the current champion. Al retains his championship unless a second round is required and the challenger beats Al in both games. If Al wins the initial game of the second round, no more games are played.

Furthermore, we know the following:

- The probability that Bo will beat Ci in any particular game is 0.6.
- The probability that Al will beat Bo in any particular game is 0.5.
- The probability that Al will beat Ci in any particular game is 0.7.

Assume no tie games are possible and all games are independent.

1. Determine the a priori probabilities that
   (a) the second round will be required.
   (b) Bo will win the first round.
   (c) Al will retain his championship this year.
2. Given that the second round is required, determine the conditional probabilities that
   (a) Bo is the surviving challenger.
   (b) Al retains his championship.
3. Given that the second round was required and that it comprised only one game, what is the conditional probability that it was Bo who won the first round?


## Solution

![img](D:\Study\Mooc\6.431x\Unit 2 Conditioning and independence\Solved problems\recitation_chess_problem_sol.jpg)



# 3 A coin tossing puzzle
**A coin tossing puzzle.** A coin is tossed twice. Alice claims that the event of getting two Heads is at least as likely if we know that the first toss is Heads than if we know that at least one of the tosses is Heads. Is she right? Does it make a difference if the coin is fair or unfair? How can we generalize Alice's reasoning?


# 4 The Monty Hall problem
**The Monty Hall problem.** This is a much discussed puzzle, based on an old American game show. You are told that a prize is equally likely to be found behind any one of three closed doors in front of you. You point to one of the doors. A friend opens for you one of the remaining two doors, after making sure that the prize is not behind it. At this point, you can stick to your initial choice, or switch to the other unopened door. You win the prize if it lies behind your final choice of a door. Consider the following strategies:

- Stick to your initial choice.
- Switch to the other unopened door.
- You first point to door 1. If door 2 is opened, you do not switch. If door 3 is opened, you switch.

Which is the best strategy?


# 5 A random walker
**A random walker.** Imagine a drunk tightrope walker, who manages to keep his balance, but takes a step forward with probability p and takes a step back with probability (1−p).

(a) What is the probability that after two steps, the tightrope walker will be at the same place on the rope as where he started?

(b) What is the probability that after three steps, the tightrope walker will be one step forward from where he started?

(c) Given that after three steps he has managed to move ahead one step, what is the probability that the first step he took was a step forward?



![img](D:\Study\Mooc\6.431x\Unit 2 Conditioning and independence\Solved problems\recitation_random_walker_sol.jpg)



# 6 Communication over a noisy channel
**Communication over a noisy channel.** A source transmits a message (a string of symbols) over a noisy communication channel. Each symbol is 0 or 1 with probability p and 1−p, respectively, and is received incorrectly with probability ϵ0 and ϵ1, respectively (see the figure below). Errors in different symbol transmissions are independent.

![On the left there are two points. The top one is labeled 0; and the bottom one is labeled 1. On the right, there are also two points, again with the top one labeled 0 and the bottom one labeled 1. Each point on the left connected to the each point on the right by a line; hence, a total of four lines. The line connecting the left 0 to right 1 is labeled epsilon_0; the line connecting the left 0 to right 0 is entitled 1-epsilon_0; the line connecting the left 1 to right 0 is labeled epsilon_1; and the line connecting the left 1 to right 1 is entitled 1-epsilon_1.](D:\Study\Mooc\6.431x\Unit 2 Conditioning and independence\Solved problems\images_Pr_1_7abd.jpg)

(a) What is the probability that the kth symbol is received correctly?

(b) What is the probability that the string of symbols 1011 is received correctly? 

(c) In an effort to improve reliability, each symbol is transmitted three times and the received string is decoded by majority rule. In other words, a 0 (or 1) is transmitted as 000 (or 111, respectively), and it is decoded at the receiver as a 0 (or 1) if and only if the received three-symbol string contains at least two 0's (or 1's, respectively). What is the probability that a 0 is correctly decoded?

(d) For what values of ϵ0 is there an improvement in the probability of correct decoding of a 0 when the scheme of part (c) is used? 

(e) Suppose that the scheme of part (c) is used. What is the probability that a symbol was 0 given that the received string is 101?



# 7 Network reliability
**Network reliability.** An electrical system consists of identical components, each of which is operational with probability p, independent of other components. The components are connected in three subsystems, as shown in the figure. The system is operational if there is a path that starts at point A, ends at point B, and consists of operational components. What is the probability of this happening?

![Three subsystems of an electrical system are connected in series from point A to point B. The first subsystem, on the right, consists of 1 component only. This is then connected to a second, more complex, subsystem in the middle. This middle subsystem consists of 3 components connected in parallel, then as a whole connected in series to another single component, and that whole combination connected in parallel to another single component. This middle subsystem is then connected on its right to the third, less complex, subsystem. This third subsystem consists of two components connected in parallel, and the whole parallel combination is connected on the right to the point B. ](D:\Study\Mooc\6.431x\Unit 2 Conditioning and independence\Solved problems\images_Network_reliability.jpg)