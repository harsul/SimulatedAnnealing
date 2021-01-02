# SimulatedAnnealing

Problem-1 – Continuous Optimization

This is the six hump camelback function with two decision variables where x lies between -3,3
and y lies between -2,2. The objective is to minimize z. The global minimum lies at (-0.0898,
0.7126) where z = -1.0316

def fitness_function (x, y) :
    return (4-2.1*pow(x,2)+pow(x, 4)/3)*pow(x,2)+x*y+(-4+4*pow(y,2))*pow(y,2)
    
    

Problem2- Continuous Optimization

def fitness_function (x, y) :
    return 3*(1-x)**2*exp(-x**2-(y+1)**2)-10*(x/5-x**3-y**5)*exp(-x**2-y**2)-exp(-(x+1)**2-y**2)/3

