import numpy as np
import time


def load_data():
    """
    Generate x and y values
    """
    raw = np.stack(np.meshgrid(range(0,100), ["+","-"], range(0,100)), axis = -1).reshape(-1,3)
    
    #Generate x from raw data
    x = np.full((len(raw), 5), 12)
    y = np.full((len(raw),4),12)

    for sample in range(len(raw)):
        #Encoding raw input onto x
        k = 0
        for i in raw[sample]:
            for j in i:
                if j == '+' :
                    x [sample, k] = 10
                elif j == '-':
                    x [sample, k] = 11
                else:
                    x [sample, k] = j 
                k = k+1
        
        #Calculate raw input and encoding output onto y
        equation = raw[sample][0]+raw[sample][1]+raw[sample][2]
        result = eval(equation)
        k = 0
        if result>=0:
            result = '+'+str(result)
        for i in str(result):
            if i == '+':
                y[sample,k] = 10
            elif i == '-':
                y[sample,k] = 11
            else:
                y[sample,k] = i
            k = k +1    
    return x, y

start = time.time()
load_data()
print(time.time()-start)