#   Name: iterating
#   Desc:  iterating over a list
#   Author: Helen Fagan
flowers =  [ "Pansy", "Bluebell", "Crocus", ]
for name in  flowers:
    print(name);

amount = len(flowers)
i = 0
while ( i < amount):
    print(str(i+1) + ". " +  flowers[i])
    i = i+1

for  i,name in enumerate(flowers):
    print( str(i +1) + "." + name)


