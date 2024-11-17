l=['dress','pants']
t=(24,52,84)
#list can be updated as per the requirements
l.append('tops')
l.extend(['Kurtis','Pyjama set'])
l.insert(2,'scarf')
print(l)
l.pop(2)
l.remove('pants')
print(l)
l.sort()
l.reverse()
print(l) 
#tuple can not be updated or changed as it is immutable
t[2]=39
print(t)