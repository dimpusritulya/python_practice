s1=set()
s2=set()
s1.add(3)
s1.update({2,3,1,5,22,634})
s2.update({1,3,53,5,7,9})
s1.remove(2)
s2.remove(53)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))