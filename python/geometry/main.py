from square import square_area, square_perimeter
from circle import circle_area, circle_perimeter

# Square calculations
side = 4
square = {
    "side": side,
    "area": square_area(side),
    "perimeter": square_perimeter(side)
}
print("Square:", square)

# Circle calculations
radius = 5
circle = {
    "radius": radius,
    "area": circle_area(radius),
    "perimeter": circle_perimeter(radius)
}
print("Circle:", circle)