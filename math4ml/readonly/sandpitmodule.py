
# coding: utf-8

# In[1]:

# Following imports pylab notebook without giving the user rubbish messages
import os, sys
stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')
get_ipython().magic('pylab notebook')
sys.stdout = stdout

from scipy.optimize import differential_evolution, minimize
import matplotlib.lines as mlines
from matplotlib.legend_handler import HandlerLine2D
from scipy.misc import imread
import matplotlib.cm as cm
from matplotlib.colors import LinearSegmentedColormap

import ipywidgets as widgets
from IPython.display import display, Markdown

matplotlib.rcParams['figure.subplot.left'] = 0
#matplotlib.rcParams['figure.figsize'] = (7, 6)

class Sandpit:
    def __init__(self, f):
        # Default options
        self.game_mode = 0 # 0 - Jacobian, 1 - Depth Only, 2 - Steepest Descent
        self.grad_length = 1/5
        self.grad_max_length = 1
        self.arrowhead_width = 0.1
        self.arrow_placement = 2 # 0 - tip, 1 - base, 2 - centre, 3 - tail
        self.tol = 0.15 # Tolerance
        self.markerColour = (1, 0.85, 0)
        self.contourCM = LinearSegmentedColormap.from_list("Cmap", [
            (0., 0.00505074, 0.191104),
            (0.155556, 0.0777596,   0.166931),
            (0.311111, 0.150468, 0.142758),
            (0.466667, 0.223177,   0.118585),
            (0.622222, 0.295886, 0.094412),
            (0.777778, 0.368595,   0.070239),
            (0.822222, 0.389369, 0.0633324),
            (0.866667, 0.410143,   0.0564258),
            (0.911111, 0.430917, 0.0495193),
            (0.955556, 0.451691,   0.0426127),
            (1., 0.472465, 0.0357061)
            ], N=256)
        self.start_text = "**Click anywhere in the sandpit to place the dip-stick.**"
        self.win_text = "### Congratulations!\nWell done, you found the phone."
        
        # Initialisation variables
        self.revealed = False
        self.handler_map = {}
        self.nGuess = 0
        self.msgbox = widgets.Output()
        
        # Parameters
        self.f = f # Contour function
        x0 = self.x0 = differential_evolution(lambda xs: f(xs[0], xs[1]), ((0,6),(0,6))).x
        x1 = differential_evolution(lambda xs: -f(xs[0], xs[1]), ((0,6),(0,6))).x
        f0 = f(x0[0], x0[1])
        f1 = f(x1[0], x1[1])
        self.f = lambda x, y: 8 * (f(x, y) - f1) / (f1 - f0) - 1
        self.df = lambda x, y: np.array([self.f(x+0.01,y)-self.f(x-0.01,y), self.f(x,y+0.01)-self.f(x,y-0.01)]) / 0.02
        self.d2f = lambda x, y: np.array([
            [ self.df(x+0.01,y)[0]-self.df(x-0.01,y)[0], self.df(x,y+0.01)[0]-self.df(x,y-0.01)[0] ],
            [ self.df(x+0.01,y)[1]-self.df(x-0.01,y)[1], self.df(x,y+0.01)[1]-self.df(x,y-0.01)[1] ]
        ]) / 0.02
           
    def draw(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim([0,6])
        self.ax.set_ylim([0,6])
        self.ax.set_aspect(1)
        self.fig.canvas.mpl_connect('button_press_event', lambda e: self.onclick(e))
        self.drawcid = self.fig.canvas.mpl_connect('draw_event', lambda e: self.ondraw(e))
        
        self.leg = self.ax.legend(handles=[] , bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="Depths:")
        img = imread("readonly/sand.png")
        self.ax.imshow(img,zorder=0, extent=[0, 6, 0, 6], interpolation="bilinear")
        display(self.msgbox)
        
    def onclick(self, event):
        if (event.button != 1):
            return
        x = event.xdata
        y = event.ydata
        
        self.placeArrow(x, y)

        if np.linalg.norm(self.x0 - [x,y]) <= self.tol:
            self.showContours()
            return
        lx = minimize(lambda xs: self.f(xs[0], xs[1]), np.array([x,y])).x
        if np.linalg.norm(lx - [x,y]) <= self.tol:
            self.local_min(lx[0], lx[1])
            return

        i = 5
        if self.game_mode == 2:
            while i > 0 :
                i = i - 1
                dx = self.next_step(self.f(x, y), self.df(x, y), self.d2f(x, y))
                self.ax.plot([x, x+dx[0]],[y, y+dx[1]], '-', zorder=15, color=(1,0,0,0.5), ms=6)
                x += dx[0]
                y += dx[1]
                if x < 0 or x > 6 or y < 0 or y > 6 :
                    break
                self.placeArrow(x, y, auto=True)
                if np.linalg.norm(self.x0 - [x,y]) <= self.tol:
                    self.showContours()
                    break
                lx = minimize(lambda xs: self.f(xs[0], xs[1]), np.array([x,y])).x
                if np.linalg.norm(lx - [x,y]) <= self.tol:
                    self.local_min(lx[0], lx[1])
                    break
            
    def ondraw(self, event):
        self.fig.canvas.mpl_disconnect(self.drawcid) # Only do this once, then self destruct the event.
        self.displayMsg(self.start_text)

    def placeArrow(self, x, y, auto=False):
        d = -self.df(x,y) * self.grad_length
        dhat = d / np.linalg.norm(d)
        d = d * np.clip(np.linalg.norm(d), 0, self.grad_max_length) / np.linalg.norm(d)

        if self.arrow_placement == 0: # tip
            off = d + dhat * 1.5 * self.arrowhead_width
        elif self.arrow_placement == 1: # head
            off = d
        elif self.arrow_placement == 2: # centre
            off = d / 2
        else: # tail
            off = array((0, 0))

        if auto:
            self.ax.plot([x],[y], 'yo', zorder=25, color="red", ms=6)
        else:
            self.nGuess += 1
            
            p, = self.ax.plot([x],[y], 'yo', zorder=25, label=
                str(self.nGuess) + ") %.2fm" % self.f(x,y), color=self.markerColour, ms=8, markeredgecolor="black")

            if (self.nGuess <= 25) :
                self.ax.text(x + 0.2*dhat[1], y - 0.2*dhat[0], str(self.nGuess))

                self.handler_map[p] = HandlerLine2D(numpoints=1)

                self.leg = self.ax.legend(handler_map=self.handler_map,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title="Depths:") 

                if (self.nGuess == 22 and not self.revealed) :
                    self.displayMsg("**Hurry Up!** The supervisor has calls to make.")
            elif not self.revealed: 
                self.showContours()
                self.displayMsg("**Try again.** You've taken too many tries to find the phone. Reload the sandpit and try again.")
        
        if self.game_mode != 1:
            self.ax.arrow(x-off[0],y-off[1], d[0], d[1],
                linewidth=1.5, head_width=self.arrowhead_width,
                head_starts_at_zero=False, zorder=20, color="black")

    def showContours(self):
        if self.revealed:
            return
        x0 = self.x0
        X, Y = np.meshgrid(np.arange(0,6,0.05), np.arange(0,6,0.05))
        self.ax.contour(X, Y, self.f(X,Y),10, cmap=self.contourCM)
        img = imread("readonly/phone2.png")
        self.ax.imshow(img,zorder=30, extent=[x0[0] - 0.375/2, x0[0] + 0.375/2, x0[1] - 0.375/2, x0[1] + 0.375/2], interpolation="bilinear")
        self.displayMsg(self.win_text)
        self.revealed = True
    
    def local_min(self, x, y) :
        img = imread("readonly/nophone.png")
        self.ax.imshow(img,zorder=30, extent=[x - 0.375/2, x + 0.375/2, y - 0.375/2, y + 0.375/2], interpolation="bilinear")
        if not self.revealed:
            self.displayMsg("**Oh no!** You've got stuck in a local optimum. Try somewhere else!")
    
    def displayMsg(self, msg):
        self.msgbox.clear_output()
        with self.msgbox:
            display(Markdown(msg))
        

