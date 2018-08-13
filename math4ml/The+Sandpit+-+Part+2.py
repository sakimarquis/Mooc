
# coding: utf-8

# # The Sandpit - Part 2
# In this notebook, we'll explore some more sandpit scenarios in order to build on your intuition of the Jacobian and gradient descent.
# We'll look at some harder scenarios and some of the pitfalls and limitations of following the gradient down contours in order to find the minimum of a function.
# 
# There is no grading for this exercise, when you are finished, close this tab to return to the course.
# 
# ## Multiple Minima
# In this sandpit, there are many local minima that the supervisor's phone could have fallen into.
# The phone is in the deepest one - Try and find it!
# 
# (You may get lucky and find the basin of the deepest minimum quickly, if you seem stuck, click somewhere else at random!)

# In[2]:

# Click into this cell and press [Shift-Enter] to start.
get_ipython().magic('run "readonly/sandpit-exercises.ipynb"')
sandpit_multiple_minima()


# ## Noisy Functions
# 
# Before the sand was loaded into this next pit, the pit floor was covered with rocks.
# This means when the supervisor tries to measure the slope, the surface they measure is rough and can change quickly.
# 
# Try to find the phone in this situation. You may notice that it is frustratingly harder to do so, as the roughness may generate more local minima.

# In[2]:

# Click into this cell and press [Shift-Enter] to continue.
get_ipython().magic('run "readonly/sandpit-exercises.ipynb"')
sandpit_rocks()


# ## Narrow Wells
# 
# In this pit, there is a deep but narrow well that the phone may have fallen into.
# See if you can find the phone in this case.

# In[3]:

# Click into this cell and press [Shift-Enter] to continue.
get_ipython().magic('run "readonly/sandpit-exercises.ipynb"')
sandpit_well()

