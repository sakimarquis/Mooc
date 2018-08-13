
# coding: utf-8

# # The Sandpit
# ## Jacobian
# The supervisor of a building site has dropped their mobile phone into a pit with an uneven floor, and it has rolled to the lowest point.
# To make matters worse, the pit has subsequently been filled with sand such that the phone is covered and cannot be seen.
# To find where in the pit their phone is, the supervisor has crafted a *‘dip-stick’* with a head designed to measure the slope of the floor if it is poked straight down through the sand.
# 
# By clicking on any point in the sandpit, and thereby measuring the negative of the Jacobian,
# $-\mathbf{J} = -\nabla f(\mathbf{x})$,
# at that point, try and find the supervisor's phone.
# Try to do this with as few dips as possible - the supervisor has calls to make!
# 
# There is no grading for this exercise, when you are finished, close this tab to return to the course.
# 
# Run the following cell to start the example.

# In[2]:

# Click into this cell and press [Shift-Enter] to start.
get_ipython().magic('run "readonly/sandpit-exercises.ipynb"')
sandpit_intro()


# ## Depth Only
# Before trying the dip-stick that measures the Jacobian, the supervisor had contructed a dip-stick that can only measure the depth on each dip.
# 
# Without information about the Jacobian, try and find the supervisor's phone.
# This should certainly be more difficult!

# In[3]:

# Click into this cell and press [Shift-Enter] to continue.
get_ipython().magic('run "readonly/sandpit-exercises.ipynb"')
sandpit_depth_only()


# ## More Sandpits
# In a nearby building site, another phone has been dropped into a pit.
# Use the gradient dip-stick and help out the supervisor.
# 
# You can run this example as many times as you like for a randomly generated sandpit.

# In[4]:

# Click into this cell and press [Shift-Enter] to continue.
get_ipython().magic('run "readonly/sandpit-exercises.ipynb"')
sandpit_random()


# In[ ]:



