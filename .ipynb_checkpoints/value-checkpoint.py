class Value:
    def __init__(self, data, _op='', label='', _children=()):
        self.data = data
        self._op = _op
        self._prev = set(_children)
        self.label = label
        self.grad = 0.0
        self._backward = lambda: None
        
        
    def __repr__(self) :
        return f"Value(data={self.data})"
    
    def __add__(self, other):
        out = Value(self.data + other.data, '+', _children=(self, other))
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, '*', _children=(self, other))
        return out