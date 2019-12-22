# Basic arithmetic functions.
# Arithmetic functions should be depreciated/removed.
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def square():
    print("| You selected square! Select what you would like to calculate.              |")
    print("| 1.) Area 2.) Area => Side 3.) Perimeter                                    |")
    print("| 4.) Perimeter => Side 5.) Diagonal                                         |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        a = float(input("| Enter the Side: "))
        print("| Area: ", a ** 2)
    elif selection == "2":
        print("| You selected Area => Side!")
        A = float(input("| Enter the Area: "))
        print("| Area: ", A ** 0.5)
    elif selection == "3":
        print("| You selected Perimeter!")
        a = float(input("| Enter the Side: "))
        print("| Perimeter: ", 4 * a)
    elif selection == "4":
        print("| You selected Perimeteer => Side!")
        p = float(input("| Enter the Perimeter: "))
        print("| Side: ", p / 4)
    elif selection == "5":
        print("| You selected Diagonal!")
        a = float(input("| Enter the Side: "))
        print("| Diagonal: ", (2 ** 0.5) * a)
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        square()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def rectangle():
    print("| You selected rectangle! Select what you would like to calculate.           |")
    print("| 1.) Area 2.) Area => Width 3.) Area => Length 4.) Diagonal                 |")
    print("| 5.) Perimeter 6.) Perimeter => Length 7.) Perimeter => Width               |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        l = float(input("| Enter the Length: "))
        w = float(input("| Enter the Width: "))
        print("| Area: ", l * w)
    elif selection == "2":
        print("| You selected Area => Width!")
        a = float(input("| Enter the Area: "))
        l = float(input("| Enter the Length: "))
        print("| Width: ", a / l)
    elif selection == "3":
        print("| You selected Area => Length!")
        a = float(input("| Enter the Area: "))
        w = float(input("| Enter the Width: "))
        print("| Length: ", a / w)
    elif selection == "4":
        print("| You selected Diagonal!")
        l = float(input("| Enter the Length: "))
        w = float(input("| Enter the Width: "))
        print("| Diagonal: ", ((w ** 2) + (l ** 2)) ** 0.5)
    elif selection == "5":
        print("| You selected Perimeter!")
        l = float(input("| Enter the Length: "))
        w = float(input("| Enter the Width: "))
        print("| Perimeter: ", 2 * (l + w))
    elif selection == "6":
        print("| You selected Perimeter => Length!")
        p = float(input("| Enter the Perimeter: "))
        w = float(input("| Enter the Width: "))
        print("| Length: ", (p / 2) - w)
    elif selection == "7":
        print("| You selected Perimeter => Width!")
        p = float(input("| Enter the Perimeter: "))
        l = float(input("| Enter the Length: "))
        print("| Width: ", (p / 2) - l)
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        rectangle()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def circle():
    print("| You selected circle! Select what you would like to calculate.              |")
    print("| 1.) Area 2.) Diameter 3.) Circumference 4.) Area => Radius                 |")
    print("| 5.) Circumference => Radius 6.) Diameter => Radius                         |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        r = float(input("| Enter the radius: "))
        print("| Area: ", 3.14 * (r ** 2))
    elif selection == "2":
        print("| You Selected diameter!")
        r = float(input("| Enter the radius: "))
        print("| Diameter: ", 2 * r)
    elif selection == "3":
        print("| You selected circumference!")
        r = float(input("| Enter the radius: "))
        print("| Circumference: ", 2 * 3.14 * r)
    elif selection == "4":
        print("| You selected Area => Radius!")
        a = float(input("| Enter the Area: "))
        print("| Radius: ", (a / 3.14) ** 0.5)
    elif selection == "5":
        print("| You selected Circumference => Radius!")
        c = float(input("| Enter the Circumference: "))
        print("| Radius: ", c / (2 * 3.14))
    elif selection == "6":
        print("| You selected Diameter => Radius!")
        d = float(input("| Enter the Diameter: "))
        print("| Radius: ", d / 2)
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        circle()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def triangle():
    print("| You selected triangle! Select what you would like to calculate.            |")
    print("| 1.) Area 2.) Area => Base 3.) Area => Height 4.) Perimeter                 |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        b = float(input("| Enter the Base: "))
        h = float(input("| Enter the Height: "))
        print("| Area: ", (b * h) / 2)
    elif selection == "2":
        print("| You selected Area => Base!")
        a = float(input("| Enter the Area: "))
        h = float(input("| Enter the Height: "))
        print("| Base: ", (2 * a) / h)
    elif selection == "3":
        print("| You selected Area => Height!")
        a = float(input("| Enter the Area: "))
        b = float(input("| Enter the Base: "))
        print("| Base: ", (2 * a) / b)
    elif selection == "4":
        print("| You selected Perimeter!")
        a = float(input("| Enter Side a: "))
        b = float(input("| Enter Side b: "))
        c = float(input("| Enter Side c: "))
        print("| Perimeter: ", a + b + c)
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        triangle()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def trapezoid():
    print("| You selected trapezoid! Select what you would like to calculate.           |")
    print("| 1.) Area 2.) Perimeter 3.) Area => Height 4.) Area => Base                 |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        b1 = float(input("| Enter Base a: "))
        b2 = float(input("| Enter Base b: "))
        h = float(input("| Enter Height: "))
        print("| Area: ", multiply(h, (b1 + b2) / 2))
    elif selection == "2":
        print("| You selected Perimeter!")
        b1 = float(input("| Enter Base a: "))
        b2 = float(input("| Enter Base b: "))
        c = float(input("| Enter Side c:"))
        d = float(input("| Enter Side d: "))
        print("| Perimeter:", b1 + b2 + c + d)
    elif selection == "3":
        print("| You selected Area => Height!")
        a = float(input("| Enter Area: "))
        b1 = float(input("| Enter Base a: "))
        b2 = float(input("| Enter Base b: "))
        print("| Height: ", multiply(2, a / (b1 + b2)))
    elif selection == "4":
        print("| You selected Area => Base!")
        a = float(input("| Enter Area: "))
        h = float(input("| Enter Height: "))
        b = float(input("| Enter other Base: "))
        print("| Area => Base", subtract(2 * (a / h), b))
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        trapezoid()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def hexagon():
    print("| You selected hexagon! Select what you would like to calculate.             |")
    print("| 1.) Area 2.) Perimeter 3.) Area => Side 4.) Perimeter => Side              |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        a = float(input("| Enter Side a: "))
        print("| Area: ", (3 * (3 ** 0.5) / 2) * (a ** 2))
    elif selection == "2":
        print("| You selected Perimeter!")
        a = float(input("| Enter Side a: "))
        print("| Perimeter: ", 6 * a)
    elif selection == "3":
        print("| You selected Area => Side!")
        a = float(input("| Enter the Area: "))
        print("| Side: ", (3 ** 0.25) * ((2 * (a / 9)) ** 0.5))
    elif selection == "4":
        print("| You selected Perimeter => Side!")
        p = float(input("| Enter the Perimeter: "))
        print("| Side: ", p / 6)
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        hexagon()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)

# Redo the Sphere fucntion.
def sphere():
    print("You selected sphere! If a value is not given, enter 0.")
    r = float(input("Enter the radius: "))
    pi = float(3.14159265359)
    four_thrids = float(4 / 3)
    a = float(input("Enter the surface area: "))
    v = float(input("Enter the volume: "))
    print("Volume: ", multiply(r, (r ** 2) * (pi * four_thrids)))
    print("Diameter: ", add(r, r))
    print("Surface Area: ", multiply(r, (r * 4 * pi)))
    print("Radius from Volume: ", multiply(3 ** 1 / 3, divide(100, (4 * pi) ** 1 / 3)))  # THIS IS BROKE ASF!
    print("Radius from Surface Area: ", multiply(0.5, (a / pi) ** 0.5))
    print("_" * 78)


def rhombus():
    print("| You selected rhombus! Select what you would like to calculate.             |")
    print("| 1.) Area 2.) Perimeter 3.) Side => Diagonals                               |")
    print("| 4.) Diagonals => Side 5.) Diagonals => Area 6.) Side => Perimeter          |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        q = float(input("| Enter diagonal q: "))
        p = float(input("| Enter diagonal p: "))
        print("| Area: ", divide(q * p, 2))
    elif selection == "2":
        print("| You selected Perimeter!")
        a = float(input("Enter side a: "))
        print("| Perimeter: ", 4 * a)
    elif selection == "3":
        print("| Side => Diagonals: ")
        q = float(input("| Enter diagonal q: "))
        p = float(input("| Enter diagonal p: "))
        print("| Side: ", divide((q ** 2 + p ** 2) ** 0.5, 2))
    elif selection == "4":
        print("| You selected Diagonal => Side!")
        a = float(input("| Enter Side: "))
        diag = float(input("| Enter the missing diagonal: "))
        print("| Diagonal from Side: ", subtract(4 * a ** 2, diag ** 2) ** 0.5)
    elif selection == "5":
        print("| Diagonal => Area!")
        a = float(input("| Enter the Area: "))
        diag = float(input("| Enter the missing diagonal: "))
        print("| Diagonal from Side: ", 2 * (a / diag))
    elif selection == "6":
        print("| You selected Side => Perimeter!")
        p = float(input("| Enter the Perimeter: "))
        print("| Side from Perimeter: ", p / 4)
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        rhombus()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def parallelogram():
    print("| You selected parallelogram! Select what you would like to calculate.       |")
    print("| 1.) Area 2.) Perimeter 3.) Perimeter => Base                               |")
    print("| 4.) Perimeter => Side 5.) Area => Height 6.) Area => Base                  |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        b = float(input("| Enter the Base: "))
        h = float(input("| Enter the Height: "))
        print("| Area: ", b * h)
    elif selection == "2":
        print("| You selected Perimeter!")
        b = float(input("| Enter the Base: "))
        a = float(input("| Enter the Side: "))
        print("| Perimeter: ", 2 * (a + b))
    elif selection == "3":
        print("| You Perimeter => Base!")
        p = float(input("| Enter the Perimeter: "))
        a = float(input("| Enter the Side: "))
        print("| Base: ", ((p / 2) - a))
    elif selection == "4":
        print("| You selected Perimeter => Side!")
        p = float(input("| Enter the Perimeter: "))
        b = float(input("| Enter the Base: "))
        print("| Side: ", ((p / 2) - b))
    elif selection == "5":
        print("| You selected Area => Height!")
        a = float(input("| Enter the Area: "))
        b = float(input("| Enter the Base: "))
        print("| Height: ", (a / b))
    elif selection == "6":
        print("| You selected Area => Base!")
        a = float(input("| Enter the Area: "))
        h = float(input("| Enter the Height: "))
        print("| Base: ", (a / h))
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        parallelogram()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def iso_tri():
    print("| You selected isoceles triangle! Select what you would like to calculate.   |")
    print("| 1.) Area 2.) Area => Base 3.) Area => Height 4.) Perimeter => Side         |")
    print("| 5.) Perimeter 6.) Base => Height 7.)Height => Base 8.)Perimeter => Base    |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        b = float(input("| Enter the Base:"))
        h = float(input("| Enter the Height: "))
        print("| Area: ", (b * h) / 2)
    elif selection == "2":
        print("| You selected Area => Base!")
        a = float(input("| Enter the Area: "))
        h = float(input("| Enter the Height: "))
        print("| Base: ", (2 * a) / h)
    elif selection == "3":
        print("| You selected Area => Height!")
        a = float(input("| Enter the Area: "))
        b = float(input("| Enter the Base: "))
        print("| Height: ", (2 * a) / b)
    elif selection == "4":
        print("| You selected Perimeter => Side!")
        p = float(input("| Enter the Perimeter: "))
        b = float(input("| Enter the Base: "))
        print("| Side: ", (p / 2) - (b / 2))
    elif selection == "5":
        print("| You selected Perimeter!")
        a = float(input("| Enter the Side: "))
        b = float(input("| Enter the Base: "))
        print("| Perimeter: ", 2 * a + b)
    elif selection == "6":
        print("| You selected Base => Height!")
        b = float(input("| Enter the Base: "))
        a = float(input("| Enter the Side: "))
        print("| Height: ", ((a ** 2) - ((b ** 2) / 4)) ** 0.5)
    elif selection == "7":
        print("| You selected Height => Base!")
        h = float(input("| Enter the Height: "))
        a = float(input("| Enter the Side: "))
        print("| Base: ", (2 * (((a ** 2) - (h ** 2)) ** 0.5)))
    elif selection == "8":
        print("| You selected Perimeter => Base!")
        p = float(input("| Enter the Perimeter: "))
        a = float(input("| Enter the Side: "))
        print("| Side: ", p - (2 * a))
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        iso_tri()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def quadrilateral():  # No formulae
    print("You selected quadrilateral! If a value is not given, enter 0.")


def equi_tri():
    print("| You selected equilateral triangle! Select what you would like to calculate |")
    print("| 1.) Area 2.) Perimeter 3.) Area => Side 4.) Perimeter => Side              |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        a = float(input("| Enter the Side: "))
        print("| Area: ", ((3 ** 0.5) / 4) * (a ** 2))
    elif selection == "2":
        print("| You selected Perimeter!")
        a = float(input("| Enter the Side: "))
        print("| Perimeter: ", 3 * a)
    elif selection == "3":
        print("| You selected Area => Side!")
        A = float(input("| Enter the Area: "))
        print("| Side:", ((2 / 3) * (3 ** 0.75) * (A ** 0.5)))
    elif selection == "4":
        print("| You selected Perimeter => Side!")
        p = float(input("| Enter the Perimeter: "))
        print("| Side: ", p / 3)
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        equi_tri()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def pentagram():  # No formulae
    print("You selected pentagram! If a value is not given, enter 0.")


def heptagon():
    print("| You selected regular heptagon! Select what you would like to calculate.    |")
    print("| 1.) Area 2.) Area => Side 3.) Perimeter 4.) Perimeter => Side              |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area!")
        a = float(input("| Enter the Side: "))
        print("| Area: ", (1.75 * (a ** 2) * 2.07652139657))
    elif selection == "2":
        print("| You selected Area => Side!")
        A = float(input("| Enter the Area: "))
        print("| Side: ", ((4 * A * 0.068796) ** 0.5))
    elif selection == "3":
        print("| You selected Perimeter!")
        a = float(input("| Enter the Side: "))
        print("| Perimeter: ", 7 * a)
    elif selection == "4":
        print("| You selected Perimeter => Side!")
        p = float(input("| Enter the Perimeter: "))
        print("| Side: ", p / 7)
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        heptagon()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def pentagon():
    print("| You selected pentagon! Select what you would like to calculate.            |")
    print("| 1.) Area 2.) Area => Side 3.) Perimeter 4.) Perimeter => Side              |")
    print("| 5.) Diagonal 6.) Diagonal => Side                                          |")
    print("|____________________________________________________________________________|")
    selection = input("| Select what you would like to calculate: ")
    if selection == "1":
        print("| You selected Area! ")
        a = float(input("| Enter the Side: "))
        comp = 1.72048
        print("| Area: ", comp * (a ** 2))
    elif selection == "2":
        print("| You selected Area => Side!")
        area = float(input("| Enter the Area: "))
        fr = 6.6874
        denom = 8.7717
        print("| Side: ", fr * (area ** 0.5) / denom)
    elif selection == "3":
        print("| You selected Perimeter!")
        a = float(input("| Enter the Side: "))
        print("| Perimeter: ", 5 * a)
    elif selection == "4":
        print("| You selected Perimeter => Side!")
        p = float(input("| Enter the Perimeter: "))
        print("| Perimeter: ", p / 5)
    elif selection == "5":
        print("| You selected Diagonal!")
        a = float(input("| Enter the Side: "))
        fr = 1.6180
        print("| Diagonal: ", fr * a)
    elif selection == "6":
        print("| You selected Diagonal => Side!")
        d = float(input("| Enter the Diagonal: "))
        y = 0.6180
        print("| Side: ", d * y)
    print("_" * 78)
    restart = input("| Would you like to continue with this shape? yes = 1, no = 0: ")
    if restart == "1":
        pentagon()
    elif restart == "0":
        main()
    else:
        print("Choose a valid option...")
    print("_" * 78)


def octagon():
    print("You selected octagon! If a value is not given, enter 0.")


def decagon():
    print("You selected decagon! If a value is not given, enter 0.")


def nonagon():
    print("You selected nonagon! If a value is not given, enter 0.")


def dodecagon():
    print("You selected dodecagon! If a value is not given, enter 0.")


def kite():
    print("You selected kite! If a value is not given, enter 0.")


def hexagram():
    print("You selected hexagram! If a value is not given, enter 0.")


def hendecagon():
    print("You selected hendecagon! If a value is not given, enter 0.")


def icosagon():
    print("You selected icosagon! If a value is not given, enter 0.")


def heptagram():
    print("You selected heptagram! If a value is not given, enter 0.")


def decagram():
    print("You selected decagram! If a value is not given, enter 0.")


def octagram():
    print("You selected octagram! If a value is not given, enter 0.")


def hexadecagon():
    print("You selected hexadecagon! If a value is not given, enter 0.")


def cube():
    print("You selected cube! If a value is not given, enter 0.")


def cylinder():
    print("You selected cylinder! If a value is not given, enter 0.")


def cone():
    print("You selected cone! If a value is not given, enter 0.")


def tetrahedron():
    print("You selected tetrahedron! If a value is not given, enter 0.")


def cuboid():
    print("You selected cuboid! If a value is not given, enter 0.")


def tri_prism():
    print("You selected triangular prism! If a value is not given, enter 0.")


def dodecahedron():
    print("You selected dodecahedron! If a value is not given, enter 0.")


def square_pyramid():
    print("You selected square pyramid! If a value is not given, enter 0.")


def torus():
    print("You selected torus! If a value is not given, enter 0.")


def icosahedron():
    print("You selected icosahedron! If a value is not given, enter 0.")


def octahedron():
    print("You selected octahedron! If a value is not given, enter 0.")


def ellipsoid():
    print("You selected ellipsoid! If a value is not given, enter 0.")


def hexagonal_prism():
    print("You selected hexagonal prism! If a value is not given, enter 0.")


def pentagonal_prism():
    print("You selected pentagonal prism! If a value is not given, enter 0.")


def hexagonal_pyramid():
    print("You selected hexagonal pyramid! If a value is not given, enter 0.")


def pentagonal_pyramid():
    print("You selected pentagonal pyramid! If a value is not given, enter 0.")


def octagonal_prism():
    print("You selected octagonal prism! If a value is not given, enter 0.")


def main():
    print("_" * 78)
    print("|~~~>                       Welcome to PyGeogebra 1.0!                   <~~~|")
    print("|~~~~~~>             The Simple Python Geometry Calculator            <~~~~~~|")
    print("|~~~~~~~~~>                                                        <~~~~~~~~~|")
    print("|~~~~~~~~~~~>                       Enjoy! :)                   <~~~~~~~~~~~~|")
    print("|____________________________________________________________________________|")
    # Shape Selection
    print("|________________________> 2-Dimensional Shapes <____________________________|")
    print("| 1.) Trapezoid  2.) Rhombus  3.) Parallelogram  4.) Triangle                |")
    print("| 5.) Hexagon  6.) Circle  7.) Isosceles Triangle  8.) Quadrilateral         |")
    print("| 9.) Rectangle  10.) Equilateral Triangle  11.) Pentagram  12.) Square      |")
    print("| 13.) Heptagon  14.) Pentagon  15.) Octagon  16.) Decagon                   |")
    print("| 17.) Nonagon  18.) Dodecagon  19.) Kite  20.) Hexagram                     |")
    print("| 21.) Hendecagon  22.) Icosagon  23.) Heptagram  24.) Decagram              |")
    print("| 25.) Octagram  26.) Hexadecagon                                            |")
    print("|________________________> 3-Dimensional Shapes <____________________________|")
    print("| 27.) Sphere  28.) Cube  29.) Cylinder  30.) Cone                           |")
    print("| 31.) Tetrahedron  32.) Cuboid  33.) Triangular Prism  34.) Dodecahedron    |")
    print("| 35.) Square Pyramid  36.) Torus  37.) Icosahedron  38.) Octahedron         |")
    print("| 39.) Ellipsoid  40.) Hexagonal Prism  41.) Pentagonal Prism                |")
    print("| 42.) Hexagonal Pyramid  43.) Pentagonal Pyramid  44.) Octagonal Prism      |")
    print("|____________________________________________________________________________|")
    print("| ")

    choice = input("| Choose the shape you want to work with: ")
    print("|____________________________________________________________________________|")

    # Routing [Redo this section]
    if choice == "1":
        trapezoid()
    elif choice == "2":
        rhombus()
    elif choice == "3":
        parallelogram()
    elif choice == "4":
        triangle()
    elif choice == "5":
        hexagon()
    elif choice == "6":
        circle()
    elif choice == "7":
        iso_tri()
    elif choice == "8":
        quadrilateral()
    elif choice == "9":
        rectangle()
    elif choice == "10":
        equi_tri()
    elif choice == "11":
        pentagram()
    elif choice == "12":
        square()
    elif choice == "13":
        heptagon()
    elif choice == "14":
        pentagon()
    elif choice == "15":
        octagon()
    elif choice == "16":
        decagon()
    elif choice == "17":
        nonagon()
    elif choice == "18":
        dodecagon()
    elif choice == "19":
        kite()
    elif choice == "20":
        hexagram()
    elif choice == "21":
        hendecagon()
    elif choice == "22":
        icosagon()
    elif choice == "23":
        heptagram()
    elif choice == "24":
        decagram()
    elif choice == "25":
        octagram()
    elif choice == "26":
        hexadecagon()
    elif choice == "27":
        sphere()
    elif choice == "28":
        cube()
    elif choice == "29":
        cylinder()
    elif choice == "30":
        cone()
    elif choice == "31":
        tetrahedron()
    elif choice == "32":
        cuboid()
    elif choice == "33":
        tri_prism()
    elif choice == "34":
        dodecahedron()
    elif choice == "35":
        square_pyramid()
    elif choice == "36":
        torus()
    elif choice == "37":
        icosahedron()
    elif choice == "38":
        octahedron()
    elif choice == "39":
        ellipsoid()
    elif choice == "40":
        hexagonal_prism()
    elif choice == "41":
        pentagonal_prism()
    elif choice == "42":
        hexagonal_pyramid()
    elif choice == "43":
        pentagonal_pyramid()
    elif choice == "44":
        octagonal_prism()
    else:
        print("Please choose a valid option from the listed shapes...")
        print("_" * 78)
        main()


main()

