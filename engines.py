import abc

class PricingEngine(object, metaclass = abc.ABCMeta):
    
    @abc.abstractmethod
    def calculate(self):
        """A method to implement pricing model"""
        pass
    
#------------------------------------------------------------------------------    
    
class BinomialPricingEngine(PricingEngine):
    def __init__(self, steps, pricer):
        self.__steps = steps
        self.__pricer = pricer
        
    @property
    def steps(self):
        return self.__steps
        
    @steps.setter
    def steps(self, new_steps):
        self.__steps = new_steps
        
    def calculate(self, option, data):
        return self.__pricer(self, option, data)

#------------------------------------------------------------------------------

class LSPricingEngine(PricingEngine):
    def __init__(self, steps, paths, pricer, mcarlo, regression):
        self.__steps = steps
        self.__paths = paths
#        self.__montecarlo = montecarlo
        self.__pricer = pricer
        self.__mcpath = mcarlo
        self.__regress = regression
  
    @property
    def steps(self):
        return self.__steps
        
    @steps.setter
    def steps(self, new_steps):
        self.__steps = new_steps
        
    @property
    def paths(self):
        return self.__paths
        
    @paths.setter
    def paths(self, new_paths):
        self.__paths = new_paths        

    @property
    def mcpath(self):
        return self.__mcpath
        
    @property
    def regress(self):
        return self.__regress
    
    def calculate(self, option, data):
        return self.__pricer(self, option, data)  

#------------------------------------------------------------------------------
if __name__ == "__main__":
    print("This is not a stand alone module")
    print("Run LSO-Main.py")    
  
