from .shape import Shape

class Rectangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        
    def compute_area(self):
        print(self._edges[0].get_length())
        return self._edges[0].get_length() * self._edges[1].get_length()
    
    def compute_perimeter(self):
        return 2*self._edges[0].get_length() + 2*self._edges[1].get_length()
    
    def compute_inner_angles(self):
        return self._inner_angles
        
class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def compute_area(self):
        return self._edges[0].get_length()**2
    
    def compute_perimeter(self):
        return 4*self._edges[0].get_length()
    
    def compute_inner_angles(self):
        return self._inner_angles