import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
from matplotlib.animation import FuncAnimation
from matplotlib import animation
from matplotlib import rc
from IPython.display import HTML
from matplotlib.animation import FuncAnimation, PillowWriter
from IPython.display import HTML
from JSAnimation.IPython_display import display_animation
from matplotlib.animation import FuncAnimation, PillowWriter


# create a figure and axes
fig = plt.figure(figsize=(12,5))
ax1 = plt.subplot(1,2,1)   
ax2 = plt.subplot(1,2,2)
# set up the subplots as needed
ax1.set_xlim(( 0, 10))            
ax1.set_ylim((0, 10))
ax1.set_xlabel('Time')
ax1.set_ylabel('Magnitude')
ax2.set_xlim((0,10))
ax2.set_ylim((0,8))
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Phase Plane')
# Create objects that will change in the animation. 
# Initially empty, have new values in the animation.

txt_title = ax1.set_title('')
line1, = ax1.plot([], [], 'silver', lw=2)     
# ax.plot returns a list of 2D line objects
# pt1, = ax2.plot([], [], 'k.', ms=2)
line3, = ax2.plot([], [], 'grey', lw=2)
ax1.legend(['sin','cos'])

def drawframe(n):
    x = [1,2,3]
    print('x',x)
    y1 = np.array([[1, 2], [3, 4], [5, 6]])

    print('y1',y1)

    y2 = np.array([[1, 2], [3, 4], [5, 6]])
    print('y2',y2)


    line1.set_data(y2, y1)
    line3.set_data(x, y1)
    # pt1.set_data(x, y2)
    txt_title.set_text('Frame = {0:4d}'.format(n))
    return (line1,)

anim = animation.FuncAnimation(fig, drawframe,  frames=100,interval=200, blit=True )


# 1. render and display the desired animation by HTML
from IPython.display import HTML
print('execute2')



from matplotlib.animation import PillowWriter
writer = PillowWriter(fps=30)
anim.save("sine_example.gif", writer=writer)