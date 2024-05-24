def triangle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort(reverse=True)
    print(sides)
    sss=sides[1]*sides[1]+sides[2]*sides[2]
    if sss==sides[0]*sides[0]:
        print("Its right triangle")
    else:
        print("its not")
# a=10
# b=20
# c=15
triangle(3,5,4)