from bird import Bird

class Seabird(Bird):
    
    def __init__(self, kind,call, diving_depth):
        super(Seabird,self).__init__(kind, call)
        self.diving_depth =  diving_depth
        
    def get_diving_depth(self):
        return self.diving_depth
        
    def get_description(self):
        return super(Seabird, self).get_description() +"\nand dives to a depth of {0} metres".format(self.diving_depth)
