from shape.rectangle import Rectangle, Square
from shape.triangle import EquilateralTriangle, IsoscelesTriangle, ScaleneTriangle, RectangleTriangle
from shape.shape import Point

### Test
## Square

square = Square ([Point(0,0), Point(0,1), Point(1,1), Point(1,0)])
print("Cuadrado")
print(f"El área del cuadrado es {square.compute_area()}")
print(f"El perímetro del cuadrado es {square.compute_perimeter()}")
print(f"Los ángulos internos son {square.compute_inner_angles()}""\n")

## Rectangle
print("Rectángulo")
rectangle = Rectangle ([Point(0,0), Point(0,4), Point(2,4), Point(2,0)])
print(f"El área del rectángulo es {rectangle.compute_area()}")
print(f"El perímetro del rectángulo es {rectangle.compute_perimeter()}")
print(f"Los ángulos internos son {rectangle.compute_inner_angles()}""\n")

## Equilateral Triangle
print("Triángulo Equilátero")
eq_triangle = EquilateralTriangle ([Point(2,0), Point(4,0), Point(3, 2)])
print(f"El área del triángulo equilátero es {eq_triangle.compute_area()}")
print(f"El perímetro del triángulo equilátero es {eq_triangle.compute_perimeter()}")
print(f"Los ángulos internos son {eq_triangle.compute_inner_angles()}" "\n")


## Isosceles Triangle
iso_triangle = IsoscelesTriangle ([Point(3,1), Point(9,1), Point(6,4)])
print("Triángulo Isósceles")
print(f"El área del triángulo isósceles es {iso_triangle.compute_area()}")
print(f"El perímetro del triángulo isósceles es {iso_triangle.compute_perimeter()}")
print(f"Los ángulos internos son {iso_triangle.compute_inner_angles()}" "\n")

## Scalene Triangle
sca_triangle = ScaleneTriangle ([Point(3,5), Point(11,6), Point(8,8)])
print("Triángulo Escaleno")
print(f"El área del triángulo escaleno es {sca_triangle.compute_area()}")
print(f"El perímetro del triángulo escaleno es {sca_triangle.compute_perimeter()}")
print(f"Los ángulos internos son {sca_triangle.compute_inner_angles()}" "\n")

## Rectangle Triangle
rect_triangle = RectangleTriangle ([Point(6,3), Point(12,3), Point(6,8)])
print("Triángulo Rectángulo")
print(f"El área del triángulo rectángulo es {rect_triangle.compute_area()}")
print(f"El perímetro del triángulo rectángulo es {rect_triangle.compute_perimeter()}")
print(f"Los ángulos internos son {rect_triangle.compute_inner_angles()}")
