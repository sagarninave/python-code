name = ["sagar", 'sanket','onkar', 'shubham']
for f in name:
    print(f, len(f))
print("\n")
    
for f in name[:2]:
    print(f, len(f))
print("\n")

for i, f in enumerate(name): # indexing start with 0
	print(i, f)
print("\n")


for i, f in enumerate(name, start=1): # indexing start with 1
	print(i, f)
print("\n")

for x in range(5):
    print(x)
print("\n")

for x in range(5,11):
    print(x)
print("\n")

for x in range(1,10,2):
    print(x)
print("\n")

for d in range(10,1,-1):
    print(d)
print("\n")



j=[4,5,6]
i=[1,2,3]
for j in (1, 6):
    print (j)


