import matplotlib.pyplot as plt
import pandas as pd
import math
## command to install all the packages
## pip3 install -r requirements.txt
## pip freeze > requirements.txt

from matplotlib.animation import FuncAnimation

from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from matplotlib import animation

data = pd.read_excel('data/sample.xlsx')
sensor_values=pd.DataFrame(data, columns=['s1','s2','s3','s4'])
df = pd.DataFrame(data, columns=['s1','s2','s3','s4']).to_numpy()



s1=sensor_values['s1'].to_numpy()
s2=sensor_values['s2'].to_numpy()
s3=sensor_values['s3'].to_numpy()
s4=sensor_values['s4'].to_numpy()
# print('df',df)
# print('s3',s3)
# print('s4',s4)

# print('s1',s1)
# print('s2',s2)






def animationPlot(s1,h1_min_array,s3,h2_min_array,angle_list):

    fig = plt.figure()

    
    axes1 = plt.subplot(1,2,1)   
    axes2 = plt.subplot(1,2,2)
    # axes.set_ylim(230, 2500)
    # axes.set_xlim(0, 10)
    axes1.set_title('Changes of h_min ', fontsize=20)
    axes1.set_ylabel('h_min (um)')
    axes1.set_xlabel('number of iterations')

    axes2.set_title('Changes of misaligned angle', fontsize=20)
    axes2.set_ylabel('Misaligned angle ($^\circ$C)')
    axes2.set_xlabel('number of iterations')

    # x1-axis
    # t= [0,1, 2, 3, 4, 5, 6,7] 
    t=np.arange(0,s1.size,1)

    # y1-axis
    y= h1_min_array


    # x2-axis
    second_x=np.arange(0,s3.size,1)
    # y2-axis
    second_y=h2_min_array
    
    # angle_y=np.arange(0,50,2)
    angle_test_x=t
    angle_test_y=angle_list

    # print('t',t)
    x1,y1 = [], []
   
    x2, y2=[],[]

    angle_X,angle_Y=[],[]

    # legend = plt.legend(loc='upper right')




    def animate(i):
        x1.append(t[i])
        y1.append((y[i]))

        x2.append((second_x[i]))
        y2.append((second_y[i]))

        angle_X.append((angle_test_x[i]))
        angle_Y.append((angle_test_y[i]))


        axes1.plot(x1,y1, scaley=True, scalex=True,color="blue",marker='o')
        axes1.plot(x2,y2, scaley=True, scalex=True,color="red",marker='x')

        axes2.plot(angle_X,angle_Y, scaley=True, scalex=True,color="gray",marker='^')
        legend = axes1.legend(['hmin_a', 'hmin_b'])
        axes2.legend(['angle'])
        
    

    ani = FuncAnimation(fig=fig, func=animate, interval=1000)

    plt.show()




        # angle_X.append((angle_test_x[i]))
        # angle_Y.append((angle_test_y[i]))

    # def val1(y2):
    #     print('x1',x1)
    #     return y2/5
    
    
    # def val2(x1):
    #     print('value ',x1)
    #     return x1
    
    # secax = axes.secondary_yaxis('right', functions =(val1, val2))
    # secax.set_xlabel('Radian')
    # secax.plot(t, [100,200,300,400,250,360], color = 'yellow',marker='^')
    # axes2=axes.twinx()
    
    # # axes2.set_xlim(0, 7)
    # axes2.plot(t, [100,200,300,400,250,360], color = 'yellow',marker='^')
    # axes2.set_ylabel('Angle between h1 and h2', )
    # axes2.plot([0,1,2,3,4,5,6], [10,20,30,40,50,60,70], color = 'yellow',marker='^')
        # axes2.set_ylabel('Angle between h1 and h2', )
        # secax = axes.secondary_yaxis('right',functions=)
        # secax.set_ylabel('Angle between h1 and h2')





# Eingangsgroesse sind wie folgt definiert:
theta1 = math.pi/4
theta2 = math.pi/4
# D in Einheit um
D=85000
# d in Einheit um
d=80000

B=int(input('Bearing width B = '))

# a1 und a2 sollen am Pruefstand gemessen werden, da nicht mehr moeglich ist, werden here jeweils 5000 um eingegeben.
a1=5000
a2=5000

def getVariables(s1,s2):
    X_Q = (D/2-(s2-a2))*math.sin(theta2)
    # print('X_Q',X_Q)
    X_P = -(D/2-(s1-a1))*math.sin(theta1)
    # print('X_P',X_P)
    Y_Q = -X_Q*math.tan(math.pi/2-theta2)
    # print('Y_Q',Y_Q)
    Y_P =X_P*math.tan(math.pi/2-theta1)
    # print('Y_P',Y_P)
    fi = math.atan((Y_P-Y_Q)/(X_Q-X_P))
    # print('fi',fi)
    b= math.sqrt(math.pow((X_P-X_Q),2)+math.pow((Y_P-Y_Q),2)) / 2
    # print('b',b)
    # x − This must be a numeric value in the range -1 to 1. If x is greater than 1 then it will generate an error.
    # beta= math.acos(2b/d)
    beta=math.acos(2*b/d)
    # print('beta',beta)
    alpha= math.pi/2-fi-beta
    # print('alpha',alpha)
    X_O1=X_Q-(d/2)*math.sin(alpha)
    # print('X_O1',X_O1)
    Y_O1=Y_Q+(d/2)*math.cos(alpha)
    # print('Y_O1',Y_O1)
    h_min=D/2- (math.sqrt(math.pow((X_O1),2)+math.pow((Y_O1),2)))-d/2
    print('h_min',h_min)
    return h_min


def getAngle(h1,h2):
    angle_lambda = math.atan((h2-h1)/B*h1)
    angle_lambda=angle_lambda*180/math.pi
    return angle_lambda

def main():

    h1_min_array=[]
    h2_min_array=[]
    
    for sensor in df:
        h1_min=getVariables(sensor[0],sensor[1])
        h1_min_array.append(h1_min)
        h2_min=getVariables(sensor[2],sensor[3])
        h2_min_array.append(h2_min)
        # print('sensor',sensor)
    # print('df',df)
    # print('h_min',h1_min_array,'h2_min',h2_min_array)
    # plot(s1,s2,h_min_array)
    angle_lambda_array=[]
    print('h1',h1_min_array)
    print('h2',h2_min_array)
    angle_lambda_array=np.column_stack((h1_min_array,h2_min_array))
    # print('angle',angle_lambda_array)


    angle_list=[]
    for value in angle_lambda_array:
        print('value',value)
        angle = getAngle(value[0],value[1])
        angle_list.append(angle)
    print('angle list',angle_list)

    animationPlot(s1,h1_min_array,s3,h2_min_array,angle_list)
    






main()
