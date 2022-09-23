numbers = [5,7,19,21,25,82]
searchNum = int(input("Enter number: "))
numFound = False
i = 0
while i < len(numbers) and not numFound:
  if searchNum == numbers[i]:
    print("found")
    numFound = True
  i = i + 1
