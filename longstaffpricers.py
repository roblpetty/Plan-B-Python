def LS_Pricer(engine, option, data):
    expiry = option.expiry
    spot, rate, volatility, dividend= data.get_data()
    steps = engine.steps
    paths = engine.paths  
    
    
    import numpy as np
    import matplotlib.pyplot as plt    

   
    dt = expiry / steps
    
    np.random.seed(9999)
    pricematrix = []
    for i in range(paths):
        path = engine.mcpath(spot,steps,volatility,rate, dividend,dt)
        pricematrix.append(path)
#    pricematrix.append([41,45.01156,45.9369063,47.05797,44.931695,63.447205])
#    pricematrix.append([41,43.73885,38.67513,34.413289,31.84393,35.66978])
#    pricematrix.append([41,44.69932,51.06678,52.88805,49.762314,55.75395])
#    pricematrix.append([41,38.51711,31.09636,26.36749,28.03090,27.475839])
#    pricematrix.append([41,43.64503,42.28958,46.61749,47.39257,51.397121])

    pricematrix = np.array(pricematrix)    
    
    cashflowmatrix = np.copy(pricematrix)
    cashflowmatrix[:] = option.payoff(cashflowmatrix[:])
    
    exercisematrix = np.zeros([paths,steps+1])
    for row in range(paths):
        exercisematrix[row,-1] = 1 if cashflowmatrix[row,-1] > 0 else 0
#------------------------------------------------------------------------------       
    for i in range(steps,1,-1):    
           
        cashflowvect = []    
        for row in range(paths):
            if 1.0 in exercisematrix[row,:]:
                index = np.nonzero(exercisematrix[row,:])        
                index = index[0]
                index = index[0]
                T = index - (i-1) 
                entry = cashflowmatrix[row,index]*np.exp(-rate*dt*T)
                cashflowvect.append(entry)                
            else:
                cashflowvect.append(0)
                
        Y = np.array(cashflowvect)
        X = pricematrix[:,i-1]
        todelete = []
        for row in range(paths):
            if option.payoff(X[row]) == 0:
                todelete.append(row)            
        Y = np.delete(Y, todelete, 0)
        X = np.delete(X, todelete, 0)
        intercept, beta1, beta2 = engine.regress(Y,X)
        print(beta1)
        
        continuation = np.zeros([paths,1])
        for row in range(paths):
            if cashflowmatrix[row,i-1] == 0:
                continuation[row] = 0        
            else:
                x = pricematrix[row,i-1]
                continuation[row] = intercept + beta1 * x + beta2 * x * x        
        for row in range(paths):
            if cashflowmatrix[row, i-1] > continuation[row]:
                exercisematrix[row, i-1] = 1
            else:
                exercisematrix[row, i-1] = 0                
            if exercisematrix[row, i-1] == 1:
                exercisematrix[row, i:steps+1] = 0

#------------------------------------------------------------------------------        
    discountvector = []
    for column in range(steps+1):
        discountvector.append(np.exp(-rate*dt*column))
        
    
    actualcfmatrix = cashflowmatrix[:]*exercisematrix[:]
    actualcfmatrix = actualcfmatrix[:]*discountvector[:]    
    option_price = np.sum(actualcfmatrix)/paths
         
    for i in range(paths):    
        plt.plot(pricematrix[i])
    
    plt.show()
    
    return option_price    
    
#------------------------------------------------------------------------------
if __name__ == "__main__":
    print("This is not a stand alone module")
    print("Run LSO-Main.py")    
  