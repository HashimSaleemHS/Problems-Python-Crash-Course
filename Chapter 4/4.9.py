'''4-9. Cube Comprehension:
Use a list comprehension to generate a list of the first 10 cubes.
Use a for loop to print out the value of each cube.'''
    

cubes = [number**3 for number in range(1, 11)]

for cube in cubes:
    print(cube)

