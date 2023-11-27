'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with
'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged'''

n=input("Enter String:")
snot=n.find('not')
spoor=n.find('poor')

if spoor>snot and snot>0 and spoor>0:
    print(n.replace(n[snot:(spoor+4)],'good'))
else:
    print(n)