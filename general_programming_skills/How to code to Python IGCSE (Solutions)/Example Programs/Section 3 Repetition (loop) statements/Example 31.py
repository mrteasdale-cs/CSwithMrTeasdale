# Section 3 - Repetition (Loop) Statements
# Example 31 – Using the range( ) statement

total = 0
print("Please enter the 3 test marks")
for counter in range(1,4):
 	print("Please enter test",counter)
 	mark = int(input())
 	total = total + mark
print("The total number of marks =",total)
