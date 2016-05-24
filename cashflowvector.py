import numpy as np

def cashflowvector(i, cashflowmatrix, exercisematrix, rate, dt):
    vector = []    
    for row in range(cashflowmatrix[:,0].size):
        if 1.0 in exercisematrix[row,:]:
            index = np.nonzero(exercisematrix[row,:])        
            index = index[0]
            index = index[0]
            T = index - (i-1) 
            entry = cashflowmatrix[row,index]*np.exp(-rate*dt*T)
            vector.append(entry)
            
        else:
            vector.append(0)
    
    vector = np.array(vector)
        
    return vector
    
if __name__ == "__main__":
    print("This is not a stand alone module")
    print("Run LSO-Main.py")    