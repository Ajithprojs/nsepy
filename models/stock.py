class Stock:
    def __init__(self, title, details_url):
        self.title = title
        self.details_url = details_url
    
    def details_url(self):
        return self.details_url

    def add_details(self, dict):
        self.details = dict

    def __str__(self):
        return self.title