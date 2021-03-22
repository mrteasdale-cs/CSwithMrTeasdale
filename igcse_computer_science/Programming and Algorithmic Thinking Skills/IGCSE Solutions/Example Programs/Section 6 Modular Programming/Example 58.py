# Section 6 – Modular Programming
# Example 58 – Scope

def displayScoreData(scores):
	average = sum(scores)/len(scores)
	print("Average score:",round(average,1))
	print("Scores ranged from:")
	print(min(scores),"to", max(scores))

# Main Program
average = 0
scores = [4,6,8,5,6,3,5,9,10,2,4,6,3,5]
displayScoreData(scores)
print()
print("Average score:",round(average,1))