s={201:8.9,345:9.6,678:7.6,202:7.2,304:8.5}
keys=s.keys()
v=s.values()
sum=0
for i in keys:
    sum=sum+i
print(sum)
sum=0
s.pop(304)
for i in v:
    sum=sum+i
print(sum)
s[606]=4.5
print(s)