#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      feyzi
#
# Created:     18/01/2020
# Copyright:   (c) feyzi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import matplotlib.pyplot as pl
import math as mt

# Task: Shoot a projectile with a given angle and speed and see if it hits the target circle

ao = float(input(' Give me the shooting angle in degrees: '))
vo = float(input(' Give me the shooting velocity: '))

ao = ao/180*mt.pi

xt = 0.5
yt = 0.7
R = 0.01


def Shootbullet (ao,vo,xt,yt,R):
    # Function must return the x and y trajectory of the bullet as a list
    # Function must also return boolean to say whether the target was hit
    x = []
    y = []
    yp = 0
    xp = 0
    dx = 0.01


    while xp <= 1:
        yp = xp*mt.tan(ao) - 9.81*(xp**2)/2/(vo**2)/((mt.cos(ao))**2)
        x = x +[xp]
        y = y +[yp]
        if ((yt - R) <= yp) and (yp <= (yt + R)) and ((xt-R)<= xp) and (xp<= (xt+R)):
            pl.plot(x,y,linewidth='1')
            pl.axis([0, 1, 0, 1])
            return(True)
        xp += dx
    pl.plot(x,y,linewidth='1')
    pl.axis([0, 1, 0, 1])
    return (False)


circle1 = pl.Circle((xt, yt), R, color='r',  fill= False)
fig, ax = pl.subplots()
ax.add_artist(circle1)


result = Shootbullet(ao,vo,xt,yt,R)
if (result == True):
    print('Target hit')
else:
    print('Target not hit')

















