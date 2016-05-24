import numpy as np
from scipy.stats import binom

def EuropeanBinomialPricer(engine, option, data):
    expiry = option.expiry
    spot, rate, volatility, dividend = data.get_data()
    steps = engine.steps
    nodes = steps + 1
    dt = expiry / steps
    u = np.exp(((rate-dividend) * dt) + volatility * np.sqrt(dt))
    d = np.exp(((rate-dividend) * dt) - volatility * np.sqrt(dt))
    pu = (np.exp((rate-dividend) * dt) - d) / (u - d)
    disc = np.exp(-rate * expiry)
    spotT = 0.0
    payoffT = 0.0

    for i in range(nodes):
        spotT = spot * (u ** (steps - i)) * (d **i)
        payoffT += option.payoff(spotT) * binom.pmf(steps - i, steps, pu)
    price = disc * payoffT
    
    return price
    
def AmericanBinomialPricer(engine, option, data):
    expiry = option.expiry
    spot, rate, volatility, dividend = data.get_data()
    steps = engine.steps
        
    dt = expiry / steps
    u = np.exp(((rate-dividend) * dt) + volatility * np.sqrt(dt))
    d = np.exp(((rate-dividend) * dt) - volatility * np.sqrt(dt))
    pu = (np.exp((rate-dividend) * dt) - d) / (u - d)
    pd = 1 - pu
    
    disc = np.exp(-rate * dt)    
    spot_t = []
    c = []
    
    for i in range(steps+1):
        spot_t.append(spot * (u ** (steps - i)) * (d ** i))
        c.append(option.payoff(spot_t[i]))
   
    ctree = np.zeros([steps+1,steps+1])
    ctree[:,-1] = c    
    for i in range(steps-1,-1,-1):
        for j in range(i+1):
            ctree[j,i] = (ctree[j,i+1]*pu+ctree[j+1,i+1]*pd)*disc
            ctree[j,i] = np.maximum( ctree[j,i], option.payoff(spot*(u**(i-j)*(d**j))))

    return ctree[0,0]