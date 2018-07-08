from bird import Bird

class Seabird(Bird):
    
    def __init__(self, kind,call, diving_depth):
        Bird.__init__(self, kind, call)
        self.diving_depth =  diving_depth
        
    def get_diving_depth(self):
        return self.diving_depth
