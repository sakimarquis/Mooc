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
