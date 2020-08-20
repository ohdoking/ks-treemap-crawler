class Stock:  
    
    # Class Variable  
    # ticker;
    # name;
    
    # The init method or constructor  
    def __init__(self, ticker, name):  
        # Instance Variable      
        self.ticker = ticker 
        self.name = name   

    # Retrieves instance variable      
    def getTicker(self):      
        return self.ticker

    def getName(self):      
        return self.name