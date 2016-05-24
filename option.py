import abc
import numpy as np

class Option(object, metaclass = abc.ABCMeta):
    """
    A Generic Option
    """
    
    @property
    @abc.abstractmethod
    def expiry(self):
        """Gets Expiry date"""
        pass
    
    @expiry.setter
    @abc.abstractmethod
    def expiry(self, new_expiry):
        """Sets Expiry date"""
        pass
        
    @abc.abstractmethod
    def payoff(self):
        """Gets options payoff"""
        pass
    
#==============================================================================
"""Option types"""    
#==============================================================================
    
class VanillaOption(Option):
    def __init__(self, expiry, strike, payoff):
        self.__expiry = expiry
        self.__strike = strike
        self.__payoff = payoff
        
    @property
    def expiry(self):
        return self.__expiry
    
    @expiry.setter
    def expiry(self, new_expiry):
        self.__expiry = new_expiry

    @property
    def strike(self):
        return self.__strike

    @strike.setter
    def strike(self,new_strike):
        self.__strike = new_strike
    
    def payoff(self, spot):
        return self.__payoff(self, spot)


class ExoticOption(Option):
    def __init__(self, expiry, strike, payoff):
        self.__expiry = expiry
        self.__strike = strike
        self.__payoff = payoff   

#==============================================================================
"""Option Payoffs"""    
#==============================================================================        
              
def call_payoff(option, spot):
    return(np.maximum(spot - option.strike,0.0))
    
def put_payoff(option, spot):
    return(np.maximum(option.strike - spot, 0.0))
    
#==============================================================================
"""Facade Patern"""    
#==============================================================================

class OptionFacade(object):
    """Facade Class to price an option"""

    def __init__(self, option, engine, data):
        self.option = option
        self.engine = engine
        self.data = data

    def price(self):
        return self.engine.calculate(self.option, self.data)

#------------------------------------------------------------------------------
if __name__ == "__main__":
    print("This is not a stand alone module")
    print("Run LSO-Main.py")    
  
    
    
    
    
    