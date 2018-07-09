class Bird(object):
    _the_kind =  None
    _the_call =  None
    
    def __init__(self, kind, call):
        self._the_kind =  kind
        self._the_call =  call

    def get_call(self):
        return self._the_call
    
    def get_kind(self):
        return self._the_kind
        
    def get_description(self):
        return 'A {0} goes {1}'.format(self.get_kind(), self.get_call())
        