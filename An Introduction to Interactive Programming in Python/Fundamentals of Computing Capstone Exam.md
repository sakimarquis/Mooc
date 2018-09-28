## Questions 1

Consider a function in Python whose execution terminates with the statement

`code`

None



## Questions 2

Consider the following snippet of Python code:

```python
var1 = 7

def var0(var1, var2):
    var3 = var1 + var2
    global var4
    var4 = 17
    return var3 + var4

print var0(var1, var1)
```

What global names are created during execution of this code snippet? What local names are created during execution of this code snippet?

**Global**- var0, var1, var4

**Local**- var2, var3



### False

Val1 can be both global and local variable.

**Global**- var0, var1, var4

**Local**- var1, var2, var3



## Questions 3

Which of the following Python expressions can be used as a key to a dictionary in Python?

hashable: tuple, bool, int, string

unhashable: list, set



## Questions 4

In SimpleGUI(and most other GUIs), a point on the canvas is indexed by two coordinates. Which statement below correctly characterizes the change in the position of a point on the canvas as these coordinates are varied?

Increasing the first coordinate moves the point right. Increasing the second coordinate moves the point downward.

## Questions 5

We will revisit the BankAccountclass from Quiz 6a in IIPP. Here is a slightly modified template for the BankAccountclass.

```python
class BankAccount:
    def __init__(self, initial_balance):
        """
        Creates an account with the given balance.
        """
        self._account = initial_balance
        self._fee = 0

    def deposit(self, amount):
        """
        Deposits the amount into the account.
        """
        self._account += amount


    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  
        Each withdrawal resulting in a balance of 
        less than 10 dollars (before any fees) also 
        deducts a penalty fee of 5 dollars from the balance.
        """
        self._account -= amount
        if self._account < 10:
            self._account -= 5
            self._fee += 5

    def get_balance(self):
        """
        Returns the current balance in the account.
        """
        return self._account

    def get_fees(self):
        """
        Returns the total fees ever deducted from the account.
        """
        return self._fee
```

The deposit and withdraw methods each change the account balance. The withdraw method also deducts a fee of 5 dollars from the balance if the withdrawal (before any fees) results in a balance of less than 10 dollars. Since we also have the method get_fees, you will need to have a variable to keep track of the fees paid.

Implement that BankAccountclass as described above. Here's one possible test with multiple accounts. This test should print the values 10, 5, 0, and 5.

```python
account1 = BankAccount(10)
account1.withdraw(15)
account2 = BankAccount(15)
account2.deposit(10)
account1.deposit(20)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()
```

## Questions 6

In IIPP, we used reference diagrams to visualize the behavior of Python programs that involved mutable objects such as lists. These reference diagrams can be viewed as instances of directed graphs (ala Algorithmic Thinking) in which nodes contain the data stored in the list and the directed edges correspond to references in the diagram.



```python
crazy = [1, 1]
crazy[1] = crazy[0]
```



### False

```python
crazy = [1, 1]
crazy[1] = crazy
```





## Questions 7

Consider this [submitted solution](https://www.coursera.org/learn/fundamentals-of-computing-capstone/resources/OaZzd) to the Rock-paper-scissors-lizard-Spock mini-project from IIPP. This solution is either correct or has one line of code that is in error.

If the program is correct, enter the number 0 in the box below. If the submitted program has an error, enter the number of the erroneous line as a positive integer in the box below.

Note that the lines are numbered starting at one as done in IDLE and CodeSkulptor. (Hint: IDLE displays the line number of the currently selected line in the lower right corner of the window.)

```python
difference = comp_number - player_number % 5 #66
```

## Questions 8

Consider this[submitted solution](https://www.coursera.org/learn/fundamentals-of-computing-capstone/resources/0HZKB)to the Pong mini-project from IIPP. Note that the paddles do not move in response to key presses.

Modifying four consecutive lines of code fixes this problem and yields a working program. Enter the line number of the first line of code that needs to be modified. Again, the lines are numbered starting at one as done in IDLE or CodeSkulptor.

    # 64 ~ 67
    canvas.draw_line([HALF_PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT ],
                [HALF_PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT], PAD_WIDTH , "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT],
                [WIDTH - HALF_PAD_WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT], PAD_WIDTH, "White")

## Questions 9

Consider this[submitted solution](https://www.coursera.org/learn/fundamentals-of-computing-capstone/resources/1MQK0)to the Blackjack mini-project from IIPP. Note that the program throws an `AttributeError`.

Modifying exactly one line of the program corrects this error and yields a program that works correctly. Enter the number of the line of code that needs to be modified. Again, the lines are numbered starting at one as done in IDLE or CodeSkulptor.

```python
# 86 
self.deck.append(Card(suit, rank))
```

## Question 10

Consider the following sequence of operations on a stack. In this sequence*Add*(5) means to push 5 onto a stack.*Rem*() means to pop an element off of a stack.

*Add*(4),*Add*(8),*Rem*(),*Add*(7),*Add*(6),*Add*(5),*Rem*(),*Rem*(),*Add*(2),*Rem*(),*Add*(3),*Add*(7)

Perform these operations on an initially empty stack. What are the contents of the stack after all of these operations are complete?

Indicate your answer with a single number in which each digit is an element on the stack. The right-most element (the least significant digit) should be the next element to be popped. For example, 321 would indicate a stack with three elements (3, 2, and 1) and 1 would be the next element to be popped.

```python
class Stack():
    def __init__(self):
        self._stack = []

    def Add(self, ele):
        self._stack += [ele]

    def Rem(self):
        length = len(self._stack)
        self._stack.pop(length - 1)

    def __str__(self):
        return str(self._stack)

s = Stack()
s.Add(4)
s.Add(8)
s.Rem()
s.Add(7)
s.Add(6)
s.Add(5)
s.Rem()
s.Rem()
s.Add(2)
s.Rem()
s.Add(3)
s.Add(7)

print s

"""
[4, 7, 3, 7]

ans = 4737
"""
```

## Questions 11

What is the probability of rolling a Yahtzee (five of a kind) on a single roll of 5 six-sided dice?

Enter a single numerical answer with at least four significant digits of precision below

$6×(1/6)^5 = 0.000771604938272$

## Questions 12

Assume you have an unfair die. The die has a0.10.1probability of landing on 1, a0.20.2probability of landing on 2, a0.30.3probability of landing on 3, a0.150.15probability of landing on 4, a0.050.05probability of landing on 5, and a0.20.2probability of landing on 6.

Write a function, $\color{red}{\verb|probability(outcomes)|}$ , that takes a list of numbers as input (where each number must be between 1 and 6 inclusive) and computes the probability of getting the given sequence of outcomes from rolling the unfair die. Assume the die is rolled exactly the number of times as the length of the $\color{red}{\verb|outcomes|}$.

For example, the result of $\color{red}{\verb|probability([1])|}$ should be $\color{red}{\verb|.1|}$.

What is the result of the following call to the function?

```python
probability([4, 2, 6, 4, 2, 4, 5, 5, 5, 5, 1, 2, 2, 6, 6, 4, 6, 2, 3, 5, 5, 2, 1, 5, 5, 3, 2, 1, 4, 4, 1, 6, 6, 4, 6, 2, 4, 3, 2, 5, 1, 3, 5, 4, 1, 2, 3, 6, 1])
```

Enter a single numerical answer with at least four significant digits of precision in the box below. Note that Coursera will accept floating point numbers formatted using Python's scientific notation.

```python
PROB = [0.1, 0.2, 0.3, 0.15, 0.05, 0.2]
def probability(outcomes):
    ans = 1
    for i in outcomes:
        ans = ans * PROB[i-1]
    return ans

print probability([1])
print probability([6])

print probability([4, 2, 6, 4, 2, 4, 5, 5, 5, 5, 1, 2, 2, 6, 6, 4, 6, 2, 3, 5, 5, 2, 1, 5, 5, 3, 2, 1, 4, 4, 1, 6, 6, 4, 6, 2, 4, 3, 2, 5, 1, 3, 5, 4, 1, 2, 3, 6, 1])

'''
ans = 2.3914845e-43
'''
```

## Questions 13

Consider a process that grows binary trees. At time step 0, the process starts with a tree, $T$, that consists of a single node. Thereafter, the following happens in each step of the process:

1. The existing tree, $T$, is copied, creating an identical tree, $S$.
2. A new root node, $R$, is created.
3. The left child of $R$ is set to $T$.
4. The right child of $R$ is set to $S$.
5. The tree rooted atRRbecomes the new $T$ for the next step of the process.

Which arithmetic sum models the number of nodes in $T$ after time step $n$?

i think ans is $1+3+7+⋯+2^{n+1} − 1$

but i choose  $1+2+4+⋯+2^n$

## Questions 14

Which math expression is equivalent to the sum that is the answer to the previous question?

$2^{n+1} − 1$

## Questions 15

Consider rooted trees in which the number of children for each node is equal to the height of the subtree rooted by the node. If the height of the root of the tree isnn, enter a math expression for the maximum number of leaves in a tree that satisfies this property.

$n!$

## Questions 16

Consider the following grid:

![](https://d396qusza40orc.cloudfront.net/foccapstone/exam_figs/gridfoc.png)

The neighbors of a particular grid square are the squares that are up, down, left, and right from that square. Black squares are blocked and cannot be searched. If you start a Breadth-first Search from square 15, which of the following are possible orders in which the squares could be searched?

For this problem, you may assume that the neighbors of a cell are represented using a set as done in "Algorithmic Thinking".

`15, 21, 9, 16, 14, 20, 10, 17, 13, 19, 4, 23, 12, 7, 5, 1, 0, 2`



### False

Consider the grid as a tree, so 13 and 20 are all 2 steps from 15.

`15, 14, 21, 9, 16, 20, 13, 10, 17, 19, 7, 12, 4, 23, 1, 5, 2, 0`

`15, 21, 9, 16, 14, 20, 10, 17, 13, 19, 4, 23, 12, 7, 5, 1, 0, 2`



## Questions 17

"Pick-A-Number" is a game in which the board consists of a list of numbers. On a player's turn, that player may pick a number on either end of the list. Turns alternate. When the list is exhausted, the winner is the player with the highest sum of the numbers they picked.

For example, consider the following game board:

3, 5, 2, 1

Players P1 and P2 play optimally as follows:

- P1 picks 1, leaving 3, 5, 2
- P2 picks 3, leaving 5, 2
- P1 picks 5, leaving 2
- P2 picks 2

P1 then wins 6 to 5.

Write a recursive function, $\color{red}{\verb|pick_a_number(board)|}$ that takes a list representing the game board and returns a tuple that is the score of the game if both players play optimally. Here, optimal play means that the player maximizes his/her final score. The returned tuple should be ordered with the current player's score first and the other player's score second.

Compute the value of the expression below:

```python
pick_a_number([12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1])
```

Enter just the two numbers with a space between them. For example, if your function returns $\color{red}{\verb|(6, 5)|}$ (as it should on the above example game), you should just enter $\color{red}{\verb|6 5|}$ in the answer box.

```python
def pick_a_number(board):
    player1 = []
    player2 = []
    board_copy = board[::]
    turn = 1
    while len(board_copy) > 0:
        first = board_copy[0]
        last = board_copy[-1]
        if first > last:
            best = first
            board_copy.pop(0)
        else:
            best = last
            board_copy.pop(-1)
        if turn == 1:
            player1.append(best)
            turn = 2
        else:
            player2.append(best)
            turn = 1   
    return (sum(player1),sum(player2))

print pick_a_number([12, 9, 7, 3, 4, 7, 4, 3, 16, 4, 8, 12, 1, 2, 7, 11, 6, 3, 9, 7, 1])

'''
>>> (75, 61)

ans = 75 61
'''
```



### False

can't figure out

maybe: 67 69



## Questions 18

Consider the following five functions:

1. $1^n+2^n+\cdots+1000^n$
2. $(n^3+2n)/(2n+1)$
3. $n^{1000}$
4. $(n^2+1)/(n+1)$
5. $(n!)^n$

Your task is to reorder the functions in the list above so that each function is big-O of the functions below it. As these functions are reordered, the initial numbers assigned to each function should be preserved.

Once you have successfully reordered the functions, enter the numbers associated with the reordered functions (ordered from top to bottom) in the box below. For example, if function 5 is big-O of function 4, function 4 is big-O of function 3,..., and function 2 is big-O of function 1, enter your answer as $\color{red}{\verb|5 4 3 2 1|}$ in the box below.

1. $1000^n$

2. $n^2$

3. $n^{1000}$

4. $n$

5. $n^n$



4 2 3 1 5



## Questions 19

Let $G=(V,E)$ be an undirected graph with $n$ nodes and $m$ edges, and let $deg(v)$ , for $v \in V$, denote the degree of node $v$. Give an expression in terms of $m$, $n$, or both, for the term $\sum_{v \in V} deg(v)$.

2*m

## Questions 20

The *transitive closure* of a directed graph $g=(V,E)$ is a directed graph $g′=(V,E′)$ such that $(u,v)∈E′$  if and only if there is a path from $u$ to $v$ in $g$. The following is a dynamic programming algorithm (incomplete) for computing the adjacency matrix, denoted by $R^{(n)}$, of the transitive closure of directed graph $g$ that is given by its adjacency matrix $A$. In this question, we assume the nodes in $V$ are numbered $1,2,\ldots,n$

![Q20](D:\Study\Mooc\An Introduction to Interactive Programming in Python\Q20.png)

The fifth line is missing the term to be assigned to $R^{(k)}$. Which of the following gives the correct term?



I guess is about how i connected to j through nodes in the graph

$R^{(k−1)}[i,j]**or**(R^{(k-1)}[i,k]**and**R^{(k-1)}[k,j])$

## Questions 21

Questions 21 - 25 refer to the following pseudo-code of Algorithm **Mystery**:

![img](D:\Study\Mooc\An Introduction to Interactive Programming in Python\ExamMysteryAlgorithm.jpg)



For some input graphs, the output of the algorithm might not be unique. If we use the following graph g1g1 as input to Algorithm **Mystery**, which of the following sets could Algorithm **Mystery** return as output?

![img](D:\Study\Mooc\An Introduction to Interactive Programming in Python\MystAlgFig1.jpg)



{3, 5, 7}

{2, 4, 6}



## Questions 22

If we use the following graph g2g2 as input to Algorithm **Mystery**, which of the following sets could Algorithm **Mystery** return as output?

![img](D:\Study\Mooc\An Introduction to Interactive Programming in Python\MystAlgFig2.jpg)



{1}



## Questions 23

Which of the following statements correctly specifies the output of Algorithm **Mystery**?



A subset V'⊆ V of minimum size such that every edge in E has at least one of its endpoints in V'.



## Questions 24

For an input graph gg with nn nodes and mm edges, that is represented by its adjacency list, which of the following terms gives the tightest bound on the worst-case running time of Lines 5–7 in Algorithm **Mystery**? Assume that testing membership of an element in a set takes O(1) operations.



O(mn)



### False

O(m + n)









