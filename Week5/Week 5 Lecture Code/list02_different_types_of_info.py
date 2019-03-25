#   Name: different_types_of_info
#   Desc: homo and heterogenous lists
#   Author: Helen Fagan
ages  = [ 5, 80, 66, 12 ]
names = [ "Amy",  "Karl", "Frank",  "Pat" ]

print(names[0] +"  is age " +  str(ages[0]) )
print(names[1] +"  is age " +  str(ages[1]) )

info  =  [   "Ann", 7 , "Church Road", "Cork" ]
print (info[0] +  " lives  in ",  info[3] )
info[0] = "Emma"
info[3] = "Dublin"
print (info[0] +  " lives  in ",  info[3] )
info.append("Ireland")
print (info[0] +  " lives  in " +  info[3] +", " + info[4])

for name in  names:
    print(name);

print(names[:])
