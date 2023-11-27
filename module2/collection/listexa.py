city=['rajkot','surat','baroda','morbi']

'''print(city)
print(city[0])
print(city[1:4])
print(city[0:2])
print(city[:3])
print(city[-1])

print(len(city))'''

'''if 'surat' in city:
    print("yes...")
else:
    print("no...")'''

#print(city.index('baroda'))

'''for i in city:
    print(i)'''

'''for i in city:
    print(f"{city}:{i.index(city)}")'''

'''n=0
for i in city:
    print(f"{n} - {i}")
    n+=1'''


#----------------------------------------#
print(city)
#city[2]='bhesan'
#city.append("gondal")
#city.pop()
#city.pop(1)
#city.remove('morbi')
#city.clear()
#city.reverse()
#city.sort()
#del city
#print(city)
#newcity=city.copy()
newcity=['gondal','ahemdabad','junagadh']
#print(newcity+city)
newcity.extend(city)
print(newcity)