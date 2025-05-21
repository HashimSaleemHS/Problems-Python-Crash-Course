'''5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
•	 Look closely at your results, and make sure you understand why each line
evaluates to True or False.
•	 Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False.'''


car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')  # True

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')  # True

print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')  # True

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')  # True

print("\nIs car == 'bmw'? I predict False.")
print(car == 'bmw')  # False

cars = ['subaru', 'audi', 'bmw']
print("\nIs 'subaru' in cars? I predict True.")
print('subaru' in cars)  # True

print("\nIs 'toyota' in cars? I predict False.")
print('toyota' in cars)  # False

print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)  # True

print("\nDoes car start with 's'? I predict True.")
print(car.startswith('s'))  # True


