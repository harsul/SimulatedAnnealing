"""
Created on Thu Nov  5 13:50:39 2020
@author: Harun
"""
from random import random, uniform
from math import pow, exp
import matplotlib.pyplot as plt
from numpy import savetxt

def fitness_function (x, y) :
    return (4-2.1*pow(x,2)+pow(x, 4)/3)*pow(x,2)+x*y+(-4+4*pow(y,2))*pow(y,2)
def random_x () :
    return uniform(-3,3)
def random_y() :
    return uniform(-2,2)

def energy_function (dEnergy, T) :
    return exp(-dEnergy/T)

#initialize the starting x,y and fitness function
x = random_x()
y = random_y()
fitness_current = fitness_function(x,y)
fitness_best = fitness_current

#set temperature at starting and ending
T_start = 200000000000
T_finish = 0.000001
CoolingRate = 0.9999 #set the cooling rate 

best_fitness_record=[] #for saving best fitness results

#the program will work until starting temperature reaches finishing temperature
while T_start > T_finish :
    #set new values randomly
    x = random_x() 
    y = random_y() 
    fitness_new = fitness_function(x, y)
    if fitness_new < fitness_current :
        #if new fitness function is smallen than current x and y will take new values
        x_current = x
        y_current = y
        fitness_current = fitness_new
        fitness_best = fitness_new
    else:
        R = random()
        dE=fitness_new-fitness_current
        if energy_function(dE, T_start) > R :
            x_current = x
            y_current = y
            fitness_current = fitness_new
            fitness_best = fitness_new
    T_start *= CoolingRate #update temperature by cooling rate
    best_fitness_record.append(fitness_best) #save new best fitness result
    
print ("x = ", x_current, "y = ", y_current)
print ("Best Fitness = ", fitness_best)

plt.plot(best_fitness_record)

savetxt('data4.csv', best_fitness_record[1::1500], delimiter=',')