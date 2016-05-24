import numpy as np
import statsmodels.api as sm

def regress(Y,X):

    if X.size == 0:
        intercept, b1, b2 = 0.0,0.0,0.0
        return intercept, b1, b2
    
    X = np.column_stack((X,X[:]*X[:]))
    X = np.insert(X, 0, 1, axis = 1)   
    
    model = sm.OLS(Y,X)
    fit = model.fit()
    
    intercept, b1, b2 = fit.params    
    return intercept, b1, b2

if __name__ == "__main__":
    print("This is not a stand alone module")
    print("Run LSO-Main.py")    
