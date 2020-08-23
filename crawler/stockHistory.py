class StockHistory:  
    
    # Class Variable  
    # ticker;
    # price;
    # date;
    
    # The init method or constructor  
    def __init__(self, id, ticker, price, date):  
        # Instance Variable      
        self.id = id
        self.ticker = ticker
        self.price = price   
        self.date = date   

    # Retrieves instance variable      
    def getId(self):      
        return self.id

    def getTicker(self):      
        return self.ticker

    def getPrice(self):
        return self.price

    def getDate(self):
        return self.date