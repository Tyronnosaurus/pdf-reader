from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
    """
    Source: https://stackoverflow.com/a/55825140/1209004
    """
    text = ""
    
    def handle_data(self, data):
        self.text += data