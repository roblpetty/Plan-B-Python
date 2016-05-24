import option as op
import engines
import marketdata as md
import longstaffpricers as lsp
import binomialpricers as bp;
import mcarlo as mc
import regression as reg

def main():
    strike = 40
    expiry = 1.
    
    spot = 41
    rate = 0.08
    volatility = 0.3
    dividend = 0.0

    steps = 365
    paths = 10000  
        
    payoff = op.put_payoff
    pricer = lsp.LS_Pricer
    mcarlo = mc.mcpath
    regression = reg.regress
    

    
    option = op.VanillaOption(expiry, strike, payoff)
    engine = engines.LSPricingEngine(steps,paths, pricer, mcarlo,regression) 
    data = md.MarketData(rate, spot, volatility, dividend)
     
    testoption = op.OptionFacade(option, engine, data)
    
    price = testoption.price()
    
    print("The price of the option is {:.3f}.".format(price))








        
if __name__ == "__main__":
    main()