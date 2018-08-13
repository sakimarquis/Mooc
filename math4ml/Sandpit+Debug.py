
# coding: utf-8

# In[117]:

# Click into this cell and press [Shift-Enter] to start.
get_ipython().magic('run "readonly/sandpit-exercises.ipynb"')
sp = sandpit_random_test()

def next_step(f, J, H) :
    gamma = 0.5
    return -gamma * J

sp.next_step = next_step
sp.game_mode=2
sp.draw()
sp.showContours()


# In[127]:

sp.revealed = False
sp.draw()
sp.nGuess = 0
sp.showContours()


# In[ ]:



