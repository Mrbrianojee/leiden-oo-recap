from bird import Bird

class Fowl(Bird):
    
    fowl_types = {'landfowl':'Landfowl is an order of heavy-bodied ground-feeding birds',
                  'waterfowl':'Waterfowl is an order of birds that comprises three families: \nAnhimidae (the screamers)\n'
                                        'Anseranatidae (the magpie goose), \nAnatidae'
                 }
    
    def __init__(self,kind,call, fowl_type):
        Bird.__init__(self, kind,call)
        self.fowl_type =  fowl_type
        
        
    def get_description(self):
        return  "Some interesting facts about the {0}. The {0} is a {1}.\n{2}".format(
            Bird.get_kind(self), 
            self.fowl_type, 
            self.fowl_types[self.fowl_type.lower()]
            )