import math

# Function to calculate the area of a circle
def circle_area(radius):
    assert radius > 0, "Radius must be positive"
    return math.pi * radius ** 2

# Function to calculate the perimeter (circumference) of a circle
def circle_perimeter(radius):
    assert radius > 0, "Radius must be positive"
    return 2 * math.pi * radius

# Example usage
radius = 5

print(f"Radius: {radius}")
print(f"Circle area: {circle_area(radius):.2f}")
print(f"Circle perimeter: {circle_perimeter(radius):.2f}")