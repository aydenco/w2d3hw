#function for use in terminal
def sq_feet():

    length = input("What is the length in feet?")
    width = input("What is the width feet?")
    total = int(length) * int(width)
    print(f"The house is {total} square feet.")

#function for use in code
def sqFeet(length, width):
    print(int(length) * int(width))

#function for use in terminal
def circ():
    radius = input("What is the radius of the circle? (Exclude units): ")
    pi = 3.141592653589793
    cir_rad = 2 * int(pi) * int(radius) 
    print(f"The circumference of the circle is {cir_rad}.")

#function for use in code
def circle_circ(radius):
    pie = 3.141592653589793
    print(2 * int(pie) * int(radius))
