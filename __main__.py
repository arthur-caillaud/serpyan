from serpyan import Array

a = [1,2,3,4,5,6]
b = Array(a)
b.map(lambda x: 2*x).map(lambda x: x+1).filter(lambda x: x%3 == 0)

print(b)
print(a)
