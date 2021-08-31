'''
A collection of functions 
for printing basic shapes
This is an introduction to MODULES
'''
CHAR='*'
def rectangle(height,width):
    '''Prints a rectangle'''
    for row in range(height):
        for col in range(width):
            print(CHAR,end='')
        print()
def square(side):
    '''Prints a square'''
    rectangle(side,side)
def triangle(height):
    '''Prints a triangle'''
    for row in range(height):
        for col in range(1,row+2):
            print(CHAR,end='')
        print()