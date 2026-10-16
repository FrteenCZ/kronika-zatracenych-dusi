from math import cos, pi, sin, sqrt

a_x: float = float(input())
a_y: float = float(input())
distance: float = float(input())
angle: float = float(input())

b_x: float = a_x + cos((angle / 360) * 2 * pi) * distance
b_y: float = a_y + sin((angle / 360) * 2 * pi) * distance

c_x: float = a_x + cos(((angle + 45) / 360) * 2 * pi) * distance * sqrt(2)
c_y: float = a_y + sin(((angle + 45) / 360) * 2 * pi) * distance * sqrt(2)

d_x: float = a_x + cos(((angle + 90) / 360) * 2 * pi) * distance
d_y: float = a_y + sin(((angle + 90) / 360) * 2 * pi) * distance

print(
    f"polygon(({a_x:.2f},{a_y:.2f}),({b_x:.2f},{b_y:.2f}),({c_x:.2f},{c_y:.2f}),({d_x:.2f},{d_y:.2f}))"
)
