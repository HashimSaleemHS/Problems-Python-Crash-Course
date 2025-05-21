'''4-5. Summing a Million:
Make a list of the numbers from 1 to 1,000,000, and then use min() and max() to make sure your list actually starts at 1 and ends at 1,000,000.
Also, use the sum() function to see how quickly Python can add a million numbers.'''


numbers= []
for num in range (1, 1000001):
    numbers.append(num)
min_num = min(numbers)    
max_num = max(numbers)
sum_numbers= sum(numbers)
print(f"Smallest Number : {min_num} \nMaximum Number :{max_num} \nSum of All Numbers : {sum_numbers}")
