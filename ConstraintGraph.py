class ConstraintGraph:
    
    def __init__(self,domain=None,constraint=None, arc=None):
        self.domain = domain
        self.constraint = constraint
        self.arc = arc

    def ac3(self):
        try:



