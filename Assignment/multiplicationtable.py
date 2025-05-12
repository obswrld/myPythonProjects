start = 1
end = 9

print(" ",end=" ")
for i in range(start, end + 1):
	print(f"{i:3}", end=" ")
print()
print("-" * 40)

for i in range(start, end + 1):
	print(f"{i:2}|", end=" ")
	for j in range(start, end + 1):
		print(f"{i * j:3}", end=" ")
	print()
