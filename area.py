def circle(radius):
    pi=3.14
    area=pi*radius*radius
    peri=2*pi*radius
    return peri,area
p,a=circle(10)
print("perimeter:",p)
print("area:",a)