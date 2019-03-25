#   Name: list_builtin_functions
#   Desc: 
#   Author: Helen Fagan
results = [80, 45, 67, 91,45]
results.sort()
results2 = results
results2[-2] = 20

miniumu_value = min(results)
maximum_value = max(results)

print(miniumu_value )
print(maximum_value )
print(results.index(miniumu_value))
print(results.index(maximum_value)+1)
n = results.count(miniumu_value)
print(n)
