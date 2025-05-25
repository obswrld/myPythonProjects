student_score1 = 50
student_score2 = 50
student_score3 = 50
student_score4 = 50

scores = [50,34, 45, 50, 25]
cart = ['banana', 33, 'juice', 2.5, ["FIsh", "palm oil"], True]
print(cart[0].upper())

print("we have", len(scores), "scores")
print(scores[2])


for score in scores:
	print(score)
	print(scores)
for index in range(len(scores)):
	print(index)

for index, value in enumerate(cart):
	print(index, value)

print(enumerate(cart))

print(list(enumerate(cart))[4])


scores.append(99)
scores.pop(1)
cart[4].insert(0, 6)
scores.extend([34, 67, 87, 65])
print(scores)
new_list = cart + scores
print(new_list)
print(scores[-1])
#slicing the list 
print(scores[0:3])
#slicing the list with intervals
print(scores[0:5:2])   








