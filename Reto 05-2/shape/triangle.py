
from .shape import Shape

class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)
        
    def compute_area(self):
        s = self.compute_perimeter()/2
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        return (s*(s-a)*(s-b)*(s-c))**0.5
    
    def compute_perimeter(self):
        pass

class EquilateralTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
    
    def compute_area(self):
        return (3**0.5/4) * self._edges[0].get_length()**2 #Deducción a partir de partir el triángulo en dos triángulos rectángulos de 30° y 60°
    
    def compute_perimeter(self):
        return 3*self._edges[0].get_length()
    
    def compute_inner_angles(self):
        return self._inner_angles
    
class IsoscelesTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        
    def compute_perimeter(self):
        return self._edges[0].get_length() + self._edges[1].get_length() + self._edges[2].get_length()
    
    def compute_area(self):
        return Triangle.compute_area(self)
    
    def compute_inner_angles(self):
        return self._inner_angles


class ScaleneTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        
    def compute_perimeter(self):
        return self._edges[0].get_length() + self._edges[1].get_length() + self._edges[2].get_length()
    
    def compute_area(self):
        return Triangle.compute_area(self)
    
    def compute_inner_angles(self):
        return self._inner_angles

class RectangleTriangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)
        
    def compute_perimeter(self):
        return self._edges[0].get_length() + self._edges[1].get_length() + self._edges[2].get_length()
    
    def compute_area(self):
        return Triangle.compute_area(self)
    
    def compute_inner_angles(self):
        return self._inner_angles