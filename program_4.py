# Program #4: Coordinates



def find_distance(a, b):
    import math
    coord1 = list(a)
    x1 = int(coord1[0])
    y1 = int(coord1[1])
    z1 = int(coord1[2])
    coord2 = list(b)
    x2 = int(coord2[0])
    y2 = int(coord2[1])
    z2 = int(coord2[2])
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z1 - z2) ** 2)
    return distance

# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.
def main():
    while True:
        try:
            coord1 = tuple(input("Enter the location of point 1. Separate coordinates by a space (x, y, z):").split())
            coord2 = tuple(input("Enter the location of point 2. Separate coordinates by a space (x, y, z):").split())
            distance = find_distance(coord1, coord2)
            print(f'The distance between the two coordinates is {distance:.2f} units.')
            break
        except ValueError:
            print("Please enter three numbers separated by spaces.")

if __name__ == "__main__":
    main()
# The mainline calls the distance function and stores the distance in a variable. The mainline then displays the distance.
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)


#This program was written on 10/17/25 by Logan Gibson
#Its name is "Three-dimensional Coordinates"