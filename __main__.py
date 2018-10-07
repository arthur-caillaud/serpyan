from serpyan import Array

print (Array.range(10000).filter(lambda x : x % 3 == 0).reduce(lambda acc, x : acc + x, 0))
