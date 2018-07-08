class Bird:
    _the_kind =  None
    _the_call =  None
    
    def __init__(self, kind, call):
        self._the_kind =  kind
        self._the_call =  call


    def call(self):
        return self._the_call
    
    def kind(self):
        return self._the_kind
        
    def description(self):
        return 'A {0} goes {1}'.format(self.kind(), self.call())
        