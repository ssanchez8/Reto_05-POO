import math

class Point:
    def __init__(self, x:int, y:int):
        self._x = x
        self._y = y
        
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def compute_distance(self, other_point):
        return ((self._x - other_point.get_x())**2 + (self._y - other_point.get_y())**2)**0.5

class Line:
    def __init__(self, point1:Point, point2:Point):
        self._length = point1.compute_distance(point2)
        self._start = point1
        self._end = point2
    
    def get_start(self):
        return self._start
    
    def get_end(self):
        return self._end
    
    def get_length(self):
        return self._length    
    
class Shape:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [Line(vertices[i], vertices[(i+1)%len(vertices)]) for i in range(len(vertices))] #Cierra la figura con el primer punto (resto de la división de i entre el número de vértices)
        self._inner_angles = self.inner_angles()
        self._is_regular = self.is_regular()
        
    def inner_angles(self):
        self._inner_angles = []
        for i in range(len(self._vertices)):
            prev_point = self._vertices[i-1]
            current_point = self._vertices[i]
            next_point = self._vertices[(i+1)%len(self._vertices)]
            a = prev_point.compute_distance(current_point)
            b = current_point.compute_distance(next_point)
            c = next_point.compute_distance(prev_point)
            angle_radians = math.acos((a**2 + b**2 - c**2)/(2*a*b))
            angle_degrees = round(math.degrees(angle_radians))
            self._inner_angles.append(angle_degrees)
        return self._inner_angles
                
    def is_regular(self):
        first_angle = self._inner_angles[0]
        for angle in self._inner_angles:
            if angle != first_angle:
                return False
        return True        
    
    def get_edges(self):
        return self._edges
    
    def get_vertices(self):
        return self._vertices
    
    def get_inner_angles(self):
        return self._inner_angles
    
    def compute_area(self):
        pass
    
    def compute_perimeter(self):
        pass
    
    def compute_inner_angles(self):
        pass