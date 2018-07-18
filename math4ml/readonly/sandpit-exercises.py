
# coding: utf-8

# In[2]:

get_ipython().magic('run "readonly/sandpitmodule.ipynb"')
  
def sandpit_intro():
    sp = Sandpit(
        lambda x,y: -((x-4.1)**2 + (y-0.9)**2) - 30*np.exp(-((x-1.5)**2 + (y-3.7)**2)/(2*1.4)),
    )
    sp.draw()
    
def sandpit_depth_only():
    sp = Sandpit(
        lambda x,y: -((x-4.1)**2 + (y-0.9)**2) - 30*np.exp(-((x-1.5)**2 + (y-3.7)**2)/(2*1.4)),
    )
    sp.game_mode = 1
    sp.win_text = """
### Congratulations!
Well done, you found the phone.

As you can see, it's much more difficult to find the bottom of the sandpit when you can only sample the depth.
Knowing the Jacobian makes it much easier to decide where to try next.
        """
    sp.draw()

def sandpit_multiple_minima():
    θ = 2 * np.pi * np.random.random()
    u0 = np.random.choice((1,3))
    v0 = np.random.choice((1,3))
    u1 = (np.random.random() - 0.5)*2/3
    v1 = (np.random.random() - 0.5)*2/3
    u = lambda x,y : (x - 3)*np.cos(θ) + (y - 3)*np.sin(θ) + 2 + u1
    v = lambda x,y : -(x - 3)*np.sin(θ) + (y - 3)*np.cos(θ) + 3 + v1
    sp = Sandpit(
        lambda x,y: 
        np.sinc(u(x, y) - 0) * np.sinc(v(x, y) - 0) +
        np.sinc(u(x, y) - 2) * np.sinc(v(x, y) - 0) +
        np.sinc(u(x, y) - 4) * np.sinc(v(x, y) - 0) +
        np.sinc(u(x, y) - 0) * np.sinc(v(x, y) - 2) +
        np.sinc(u(x, y) - 2) * np.sinc(v(x, y) - 2) +
        np.sinc(u(x, y) - 4) * np.sinc(v(x, y) - 2) +
        np.sinc(u(x, y) - 0) * np.sinc(v(x, y) - 4) +
        np.sinc(u(x, y) - 2) * np.sinc(v(x, y) - 4) +
        np.sinc(u(x, y) - 4) * np.sinc(v(x, y) - 4) +
        np.sinc(u(x, y) - 0) * np.sinc(v(x, y) - 6) +
        np.sinc(u(x, y) - 2) * np.sinc(v(x, y) - 6) +
        -np.sinc(u(x, y) - 1) * np.sinc(v(x, y) - 1) +
        -np.sinc(u(x, y) - 3) * np.sinc(v(x, y) - 1) +
        -np.sinc(u(x, y) - 1) * np.sinc(v(x, y) - 3) +
        -np.sinc(u(x, y) - 3) * np.sinc(v(x, y) - 3) +
        -np.sinc(u(x, y) - 1) * np.sinc(v(x, y) - 5) +
        -np.sinc(u(x, y) - 3) * np.sinc(v(x, y) - 5) +
        -np.sinc(u(x, y) - u0) * np.sinc(v(x, y) - v0)
    )
    sp.grad_length /= 2
    sp.win_text = """
### Congratulations!
Well done, you found the phone.

You may run this example again to find the phone in a different landscape.
Try to think of methods to avoid getting stuck in the local minima when trying to find the global minimum.
        """
    sp.draw()

def sandpit_random():
    a = np.random.rand(4, 4) *  np.outer(np.arange(4) + 1., np.arange(4) + 1.)**-2
    φx = 2 * np.pi * np.random.rand(4, 4)
    φy = 2 * np.pi * np.random.rand(4, 4)
    fn = lambda n,m,x,y: a[n,m] * np.cos(np.pi*n*x/6 + φx[n,m]) * np.cos(np.pi*m*y/6 + φy[n,m])
    ff = lambda x,y: (fn(0,0,x,y)+fn(0,1,x,y)+fn(0,2,x,y)+fn(0,3,x,y)+
        fn(1,0,x,y)+fn(1,1,x,y)+fn(1,2,x,y)+fn(1,3,x,y)+
        fn(2,0,x,y)+fn(2,1,x,y)+fn(2,2,x,y)+fn(2,3,x,y)+
        fn(3,0,x,y)+fn(3,1,x,y)+fn(3,2,x,y)+fn(3,3,x,y)+
        (1 - (x*(x - 6)*y*(y - 6))/(81))**7 / 9
        )
    sp = Sandpit(ff)
    sp.grad_length *= 1.5
    sp.win_text = """
### Congratulations!
Well done, you found the phone.

You may run this example again to find the phone in a different landscape.
        """
    sp.draw()

def sandpit_gradient(next_step) :
    a = np.random.rand(4, 4) *  np.outer(np.arange(4) + 1., np.arange(4) + 1.)**-2
    φx = 2 * np.pi * np.random.rand(4, 4)
    φy = 2 * np.pi * np.random.rand(4, 4)
    fn = lambda n,m,x,y: a[n,m] * np.cos(np.pi*n*x/6 + φx[n,m]) * np.cos(np.pi*m*y/6 + φy[n,m])
    ff = lambda x,y: (fn(0,0,x,y)+fn(0,1,x,y)+fn(0,2,x,y)+fn(0,3,x,y)+
        fn(1,0,x,y)+fn(1,1,x,y)+fn(1,2,x,y)+fn(1,3,x,y)+
        fn(2,0,x,y)+fn(2,1,x,y)+fn(2,2,x,y)+fn(2,3,x,y)+
        fn(3,0,x,y)+fn(3,1,x,y)+fn(3,2,x,y)+fn(3,3,x,y)+
        (1 - (x*(x - 6)*y*(y - 6))/(81))**7 / 9
        )
    sp = Sandpit(ff)
    sp.game_mode = 2
    sp.next_step = next_step
    sp.win_text = """
### Congratulations!
Well done, you found the phone.

You may run this example again to find the phone in a different landscape.
        """
    sp.draw()

def sandpit_rocks():
    a = np.random.rand(4, 4) *  np.outer(np.arange(4) + 1., np.arange(4) + 1.)**-2
    φx = 2 * np.pi * np.random.rand(4, 4)
    φy = 2 * np.pi * np.random.rand(4, 4)
    b = np.random.rand(4, 4) *  np.outer(np.arange(4) + 1., np.arange(4) + 1.)**-2
    θx = 2 * np.pi * np.random.rand(4, 4)
    θy = 2 * np.pi * np.random.rand(4, 4)
    fn = lambda n,m,x,y: a[n,m] * np.cos(np.pi*n*x/6 + φx[n,m]) * np.cos(np.pi*m*y/6 + φy[n,m])
    gn = lambda n,m,x,y: b[n,m]/25 * np.cos(10*np.pi*n*x/6 + θx[n,m]) * np.cos(10*np.pi*m*y/6 + θy[n,m])
    ff = lambda x,y: (fn(0,0,x,y)+fn(0,1,x,y)+fn(0,2,x,y)+fn(0,3,x,y)+
        fn(1,0,x,y)+fn(1,1,x,y)+fn(1,2,x,y)+fn(1,3,x,y)+
        fn(2,0,x,y)+fn(2,1,x,y)+fn(2,2,x,y)+fn(2,3,x,y)+
        fn(3,0,x,y)+fn(3,1,x,y)+fn(3,2,x,y)+fn(3,3,x,y)+
        (1 - (x*(x - 6)*y*(y - 6))/(81))**7 / 9 +
        gn(0,0,x,y)+gn(0,1,x,y)+gn(0,2,x,y)+gn(0,3,x,y)+
        gn(1,0,x,y)+gn(1,1,x,y)+gn(1,2,x,y)+gn(1,3,x,y)+
        gn(2,0,x,y)+gn(2,1,x,y)+gn(2,2,x,y)+gn(2,3,x,y)+
        gn(3,0,x,y)+gn(3,1,x,y)+gn(3,2,x,y)+gn(3,3,x,y)
        )
    sp = Sandpit(ff)
    sp.grad_length *= 1.5
    sp.win_text = """
### Congratulations!
Well done, you found the phone.

You may run this example again to find the phone in a different landscape.
        """
    sp.draw()
    
def sandpit_well():
    a = np.random.rand(4, 4) *  np.outer(np.arange(4) + 1., np.arange(4) + 1.)**-2
    φx = 2 * np.pi * np.random.rand(4, 4)
    φy = 2 * np.pi * np.random.rand(4, 4)
    x0 = 6 * np.random.rand()
    y0 = 6 * np.random.rand()
    fn = lambda n,m,x,y: a[n,m] * np.cos(np.pi*n*x/6 + φx[n,m]) * np.cos(np.pi*m*y/6 + φy[n,m])
    ff = lambda x,y: (fn(0,0,x,y)+fn(0,1,x,y)+fn(0,2,x,y)+fn(0,3,x,y)+
        fn(1,0,x,y)+fn(1,1,x,y)+fn(1,2,x,y)+fn(1,3,x,y)+
        fn(2,0,x,y)+fn(2,1,x,y)+fn(2,2,x,y)+fn(2,3,x,y)+
        fn(3,0,x,y)+fn(3,1,x,y)+fn(3,2,x,y)+fn(3,3,x,y)+
        (1 - (x*(x - 6)*y*(y - 6))/(81))**7 / 9 -
        0.6*np.exp(-((x-x0)**2+(y-y0)**2)/(2*0.2**2))
        )
    sp = Sandpit(ff)
    sp.grad_length *= 1.5
    sp.win_text = """
### Congratulations!
Well done, you found the phone.

You may run this example again to find the phone in a different landscape.
        """
    sp.draw()

def sandpit_random_test():
    a = np.random.rand(4, 4) *  np.outer(np.arange(4) + 1., np.arange(4) + 1.)**-2
    φx = 2 * np.pi * np.random.rand(4, 4)
    φy = 2 * np.pi * np.random.rand(4, 4)
    fn = lambda n,m,x,y: a[n,m] * np.cos(np.pi*n*x/6 + φx[n,m]) * np.cos(np.pi*m*y/6 + φy[n,m])
    ff = lambda x,y: (fn(0,0,x,y)+fn(0,1,x,y)+fn(0,2,x,y)+fn(0,3,x,y)+
        fn(1,0,x,y)+fn(1,1,x,y)+fn(1,2,x,y)+fn(1,3,x,y)+
        fn(2,0,x,y)+fn(2,1,x,y)+fn(2,2,x,y)+fn(2,3,x,y)+
        fn(3,0,x,y)+fn(3,1,x,y)+fn(3,2,x,y)+fn(3,3,x,y)+
        (1 - (x*(x - 6)*y*(y - 6))/(81))**7 / 9
        )
    sp = Sandpit(ff)
    sp.grad_length *= 1.5
    sp.win_text = """
### Congratulations!
Well done, you found the phone.

You may run this example again to find the phone in a different landscape.
        """
    sp.game_mode = 1
    return sp


# In[2]:

get_ipython().run_cell_magic('html', '', '<style>\n.output_wrapper button.btn.btn-default,\n.output_wrapper .ui-dialog-titlebar,\nspan.mpl-message {\n  display: none;\n}\n.widget-area {\n    display: table-footer-group !important;\n    position: relative;\n    top: -48px;\n}\n.output_subarea.output_markdown.rendered_html {\n    position: relative;\n    left: 8em\n}\ndiv.cell.code_cell.rendered {\n    display: table;\n}\n.widget-area button.close {\n    display: none\n}\n</style>')

