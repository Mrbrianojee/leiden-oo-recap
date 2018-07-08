class Bird:
    _the_kind =  None
    _the_call =  None
    
    def __init__(self, kind, call):
        self._the_kind =  kind
        self._the_call =  call

    def description(self):
        print('A {0} goes {1}').format(self._the_kind, self._the_call)
        