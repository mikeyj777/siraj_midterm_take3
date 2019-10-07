import requests


class Analyze:
    
    def __init__(self, company):
        self.company = company
        self.key = '4c35f1595be1213c55b1346a18a5e479'
        self.url = 'https://datafied.api.edgar-online.com/v2/corefinancials/ann?primarysymbols=' + self.company + '&appkey=' + self.key
    
    def get_fin_report(self):
        # api-endpoint 
        URL = self.url
        
        # defining a params dict for the parameters to be sent to the API 
        PARAMS = {} 
        
        # sending get request and saving the response as response object 
        r = requests.get(url = URL, params = PARAMS) 
        
        # extracting data in json format 
        self.data = r.json() 
        print(self.data)
        pass


    def data_cleanup(self):
        #keep only the Management’s Discussion and Analysis (MD&A)

        #remove all numbers
        pass
    
    def sentiment_analysis(self):
        pass