'''4-10. Slices:
Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
•	Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
•	Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
•	Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
'''

num =[1,2,3,4,5,6,7,8,9]
print ("the first three item in the list are ")
print(num[:3])
print("\nThree items from the middle of the list are:")
print(num[3:6])

print("\nThe last three items in the list are:")
print(num[-3:])

