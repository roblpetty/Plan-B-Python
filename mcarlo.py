import numpy as np

def mcpath(spot,steps,volatility, rate, dividend, dt):    
    path = [spot]
    for i in range(steps):
        drift = (rate - dividend - .5 * volatility * volatility) * dt
        diffusion =np.random.normal(0, volatility) * np.sqrt(dt)
        path.append(path[-1]*np.exp(drift + diffusion))
    return path


if __name__ == "__main__":
    print("This is not a stand alone module")
    print("Run LSO-Main.py")  