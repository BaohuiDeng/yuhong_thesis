# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation


# # First set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure()
# ax = plt.axes(xlim=(0, 10), ylim=(0, 1000))
# line, = ax.plot([], [], lw=2)


# # initialization function: plot the background of each frame
# def init():
#     line.set_data([], [])
#     return line,

# # animation function.  This is called sequentially
# def animate(i):
#     x = np.linspace(0, 2, 1000)
#     print('x',x)
#     # x=[0,1,2,3,4,5,6,7]
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     print('y',y)
#     line.set_data(x, y)
#     return line,

# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=20, blit=True)



# plt.show()




# x_data=[]
# y_data=[]
# fig, ax  =plt.subplot()
# ax.set_xlim(0,105)
# ax.set_ylim(0,12)

# line,=ax.plot(0,0)

# def animation_frame(i):
#     x_data.append(i*10)
#     y_data.append(i)

#     line.set_xdata(x_data)
#     line.set_ydata(y_data)

# animation = FuncAnimation(fig, func=animation_frame,frames=np.arange(0,10,0.01),interval=10)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# fig, ax = plt.subplots()

# x = []
# y=[]
# line, = ax.plot(x,y)


# def animate(i):
#     # x = [0,1,2,3,4,5,6,7]
#     # y=[930,930,906,670,2494,1445,1541,238]
#     x.append(i*10)
#     y.append(i)
#     line.set_xdata(x)
#     line.set_ydata(y)  # update the data.
#     return line,


# ani = animation.FuncAnimation(
#     fig, animate, interval=200, blit=True)



# plt.show()




from matplotlib import animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



fig = plt.figure(figsize=(12,8))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(230, 2500)
axes.set_xlim(0, 10)
y1= [930,930,906,670,2494,1445,1541,238] 
t= [0,1, 2, 3, 4, 5, 6,7] 
x,y = [], []


def animate(i):
    x.append(t[i])
    y.append((y1[i]))
    plt.plot(x,y, scaley=True, scalex=True, color="blue")

ani = FuncAnimation(fig=fig, func=animate, interval=1000)

plt.show()

# def plot(s1,s2,h_min_array):
#     print('plot-s1',s1,'plot-s2',s2,'plot-h_min',h_min_array)
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     X = s1
#     Y=s2
#     Z=h_min_array

#     ax.plot(X, Y, Z,color='blue',marker='o', alpha=1)

#     ax.set_xlabel('s1')
#     ax.set_ylabel('s2')
#     ax.set_zlabel('h_min')

#     plt.show()
    # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # print('plot',s1,s2,h_min_array)
    # # Make data.
    # X =s1
    # Y =s2
    # X, Y = np.meshgrid(X, Y)
    # h_min= np.array(h_min_array)
    #Z =   np.reshape(h_min,(1, h_min.size))

    # # Plot the surface.
    # # surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
    # #                     linewidth=0, antialiased=False)


    # # Customize the z axis.
    # ax.set_zlim(1,5)
    # ax.zaxis.set_major_locator(LinearLocator(10))
    # # A StrMethodFormatter is used automatically

    # ax.zaxis.set_major_formatter('{x:.02f}')

    # # Add a color bar which maps values to colors.
    # fig.colorbar(surf, shrink=0.5, aspect=5)
    # ax.set_xlabel('s1', fontsize=15, rotation=60)
    # ax.set_ylabel('s2', fontsize=15, rotation=60)
    # ax.set_zlabel('hmin', fontsize=15, rotation=60)
    # print('h_min',s1,s2,h_min_array)
    # plt.show()